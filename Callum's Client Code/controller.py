import evdev
gamepads = []
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
count = False

controllers = {"Logitech Gamepad F310","Logitech Gamepad F710","Microsoft X-Box 360 pad","Logitech Logitech Cordless RumblePad 2", "Logitech Logitech Dual Action"}
for i in devices:
    if i in controllers:
        gamepad = i
        break

#assert device.name in controllers

print("your gamepad is:",gamepad)


