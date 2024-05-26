def on_bluetooth_connected():
    basic.show_leds("""
        . . # # .
        # . # . #
        . # # # .
        # . # . #
        . . # # .
        """)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_uart_data_received():
    global data
    data = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

data = ""
basic.show_icon(IconNames.HAPPY)
bluetooth.start_uart_service()
speed = 0
angle = 90

def on_forever():
    global speed, angle
    if data == "f":
        speed += -10
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
    if data == "b":
        speed += 10
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
    if data == "l":
        angle += -5
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
    if data == "r":
        angle += 5
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
    if data == "A":
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            """)
        angle = 90
    if data == "B":
        pins.analog_write_pin(AnalogPin.P0, 0)
        pins.analog_write_pin(AnalogPin.P1, 0)
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        speed = 0
        angle = 90
    if speed > 100:
        speed = 100
    if speed < -100:
        speed = -100
    if angle < 70:
        angle = 70
    if angle > 110:
        angle = 110
    servos.P0.run(speed)
    servos.P1.set_angle(angle)
basic.forever(on_forever)
