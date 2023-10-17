import os.path
import sys
from typing import Any, Optional, List
from types import ModuleType

from diagnose.fileutils import read_source_py
from diagnose.engine.tracer import Tracer
from diagnose.typings import T_tracer_callback_func, LoggerLike

__all__ = ['PyRunner']


class DummyLoader:
    """
    The loader for the dummy module
    """

    def __init__(self, fullname: str, *args: Any) -> None:
        self.fullname = fullname


class PyRunner:
    """
    The :class:`PyRunner` is for running Python script or package from the
    cammand line.

    The idea of the class is first compiling the given source files and then
    executing the :obj:`code` with the args from the command line. When
    executing the :obj:`code`, a trace is set to collect the runtime
    information. The collected information  will be sent to the :class:`Q`
    for further using.

    Attributes:

        tracer_callbacks: The callback functions invoked in the trace. Mostly,
        it will consume the :class:`ActionMessageEntry` and produce the
        :class:`TraceMessageEntry` in the :class:`Q`

        source: The path to the executed file. To ensure the source is runnable,
        the ``PYTHONPATH`` must be set before running.

        args: The args used for the executed file.

    """
    tracer_callbacks: Optional[List[T_tracer_callback_func]] = None
    source: Optional[str] = None

    def __init__(self,
                 source: str,
                 args: List[str],
                 tracer_callbacks: Optional[List[T_tracer_callback_func]],
                 logger: LoggerLike):
        self.args = args
        self.tracer_callbacks = tracer_callbacks
        self.logger = logger
        if os.path.isabs(source):
            self.source = source
        else:
            for path in [os.curdir] + sys.path:
                if path is None:
                    continue
                f = os.path.join(path, source)
                try:
                    exists = os.path.exists(f)
                except UnicodeError:
                    exists = False
                if exists:
                    self.source = f
                    break

    def _build_module(self, source: str) -> ModuleType:
        mod_ty = ModuleType('__main__')
        mod_ty.__file__ = source
        mod_ty.__loader__ = DummyLoader
        mod_ty.__builtins__ = sys.modules['builtins']
        sys.modules['__main__'] = mod_ty
        return mod_ty

    def _build_args(self, args: List[str], source: str) -> None:
        self.origin_argv = sys.argv
        sys.argv = [source]
        for arg in args:
            sys.argv.append(arg)

    def _resume_args(self) -> None:
        sys.argv = self.origin_argv

    def _run(self, source: str, args: List[str]):
        source_byte = read_source_py(source)
        mod = self._build_module(source)
        self._build_args(args, source)
        try:
            code = compile(source_byte, source, "exec", dont_inherit=True)
        except SyntaxError:
            self.logger.error(f"Fail to compile the code: {source} due to the syntax error", exc_info=True)
            return
        except ValueError:
            self.logger.error(f"Fail to compile the code: {source} due to the inner null value", exc_info=True)
            return
        tracer = Tracer(self.tracer_callbacks, logger=self.logger)
        tracer.start()
        try:
            exec(code, mod.__dict__)
        except RuntimeError:
            self.logger.error(f"Fail to execute code: {source}", exc_info=True)
        finally:
            tracer.stop()
            self._resume_args()

    def run(self):
        assert self.source is not None
        self._run(self.source, self.args)
