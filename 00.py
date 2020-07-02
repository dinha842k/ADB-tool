from ppadb.client import Client


adb = Client(host='127.0.0.1', port=5037)

devices = adb.devices()
device = devices[0]

# png = device.screencap()

# with open('abc.png', 'wb') as f:
#     f.write(png)
device.input_tap(1054, 295)
device.input_roll()
# print(device.get_device_path())
# device.input_keyevent('1')
# device.input_text("helloaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
