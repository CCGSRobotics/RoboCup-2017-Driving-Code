import evdev
gamepads = []
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
count = False
controller_list=["Logitech Gamepad F310","Logitech Gamepad F710","Microsoft X-Box 360 pad","Logitech Logitech Cordless RumblePad 2", "Logitech Logitech Dual Action"]
for c in controller_list:
    for device in devices:
        if device.name == c:
            gamepad = device
            count = True
print("your gamepad is:",gamepad)


