bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Sad)
})
blockytalky.onReceivedString(function (key, receivedString) {
    if (receivedString == "ver") {
        basic.showIcon(IconNames.Yes)
        action = 1
        figer = input.acceleration(Dimension.Y)
    }
    if (receivedString == "dever") {
        basic.showIcon(IconNames.No)
        action = 0
        blockytalky.sendNumber("acc", 0)
    }
})
let figer = 0
let action = 0
action = 0
basic.showIcon(IconNames.Square)
basic.forever(function () {
    while (action == 1) {
        if (Math.abs(input.acceleration(Dimension.Y)) >= Math.abs(figer + 50)) {
            blockytalky.sendNumber("acc", input.acceleration(Dimension.Y))
        }
    }
    if (action == 0) {
        blockytalky.sendNumber("acc", 0)
    }
})
