bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        . . # # .
        # . # . #
        . # # # .
        # . # . #
        . . # # .
        `)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.Hash), function () {
    data = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
})
let data = ""
basic.showIcon(IconNames.Happy)
bluetooth.startUartService()
let speed = 0
let angle = 90
basic.forever(function () {
    if (data == "f") {
        speed += -20
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    }
    if (data == "b") {
        speed += 20
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    }
    if (data == "r") {
        angle += -5
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    }
    if (data == "l") {
        angle += 5
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    }
    if (data == "A") {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        angle = 90
    }
    if (data == "B") {
        pins.analogWritePin(AnalogPin.P2, 0)
        pins.analogWritePin(AnalogPin.P1, 0)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
        speed = 0
        angle = 90
    }
    if (speed > 100) {
        speed = 100
    }
    if (speed < -100) {
        speed = -100
    }
    if (angle < 70) {
        angle = 70
    }
    if (angle > 110) {
        angle = 110
    }
    servos.P2.run(speed)
    servos.P1.setAngle(angle)
})
