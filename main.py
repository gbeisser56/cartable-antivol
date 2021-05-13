def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_received_string(key, receivedString):
    global action, figer
    if receivedString == "ver":
        basic.show_icon(IconNames.YES)
        action = 1
        figer = input.acceleration(Dimension.Y)
    if receivedString == "dever":
        basic.show_icon(IconNames.NO)
        action = 0
        blockytalky.send_number("acc", 0)
blockytalky.on_received_string(on_received_string)

figer = 0
action = 0
action = 0
basic.show_icon(IconNames.SQUARE)

def on_forever():
    while action == 1:
        if abs(input.acceleration(Dimension.Y)) >= abs(figer + 50):
            blockytalky.send_number("acc", input.acceleration(Dimension.Y))
    if action == 0:
        blockytalky.send_number("acc", 0)
basic.forever(on_forever)
