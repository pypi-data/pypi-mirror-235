class Controller {
    constructor(hostname, port) {
        this.queue = []
        this.ws = new WebSocket(`ws://${hostname}:${port}`)
        this.ws.onmessage = function (message) {
            window.ctrl.queue.push(JSON.parse(message.data))
        }
        this.delay = 500
    }

    send(message) {
        this.ws.send(message)
    }

    peak() {
        return this.queue.shift()
    }

    _blink_line(classname, parent) {
        let target = document.getElementsByClassName(classname)[0]
        if (window.is_directory) {
            let showing = document.getElementsByClassName(window.showing)[0]
            showing.classList.add('invisible')
            let file_node = document.getElementsByClassName(parent)[0]
            file_node.classList.remove('invisible')
            window.showing = parent
        }

        let bgc = target.style.backgroundColor
        let rgb = bgc.replace(/^rgba?\(|\s+|\)$/g,'').split(',');
        window.scrollTo(0, target.offsetTop - 200)
        gsap.to(target, {scale: 2})
        gsap.to(target, {scale: 1, backgroundColor: `rgb(255, ${rgb[1] - 10}, ${rgb[2] - 10})`})
    }

    _enable_stop_button() {
        let stop = document.querySelector('#stop')
        stop.removeAttribute('disabled')
    }

    do_start() {
        this._enable_stop_button()
        const render = () => {
            let data = this.peak()
            if (typeof(data) === "undefined") {
                window.ctrl.do_stop()
            }
            window.ctrl._blink_line(data.classname, data.file_classname)
        }
        this.send('start')
        this.timmer = setInterval(render, this.delay)
    }

    do_pause() {
        clearInterval(this.timmer)
    }

    do_stop() {
        clearInterval(window.ctrl.timmer)
        window.ctrl.send('stop')
        document.querySelector('#control').disabled = true
        document.querySelector('#stop').disabled = true
        document.querySelector('#speed_up').disabled = true
        document.querySelector('#speed_down').disabled = true
    }

    speed_up() {
        this.delay /= 2
        this.do_pause()
        this.do_start()
    }

    speed_down() {
        this.delay *= 2
        this.do_pause()
        this.do_start()
    }
}

window.onload = () => {
    window.ctrl = new Controller('localhost', 8765)
    let control = document.querySelector('#control')
    control.innerHTML = 'START'
    control.onclick = () => {
        if (control.innerHTML === 'START') {
            control.innerHTML = 'PAUSE'
            window.ctrl.do_start()
        } else {
            control.innerHTML = 'START'
            window.ctrl.do_pause()
        }
    }
    let stop = document.querySelector('#stop')
    stop.addEventListener('click', window.ctrl.do_stop)
}