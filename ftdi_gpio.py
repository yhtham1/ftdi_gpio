
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ft232
import time


def main():
	# serial_number = "DJ5LV1RQ"
	serial_number = "DJ61E92G"
	serial_number = "DN0556IZ"  # IF314_USBIF
	serial_number = "DN6KHMZE"  # IF314_USBIF
	sp = []
	try:
		sp = ft232.Ft232(serial_number, baudrate=115200)
	except ft232.Ft232Exception:
		print("Unable to open the ftdi device: %s" % serial_number)
		sys.exit(1)

	# You may use sp as you would a Serial object
	# sp.write(b"Hello World!\n")
	# resp = sp.read(100)

	# If you want to use the CBUS pins, you enable them with cbus_setup
	# 'mask' is a bitmask which specifies which pins to enable
	# 'init' is a bitmask for the initial value for each pin
	sp.cbus_setup(mask=15, init=0)

	# Change the current value of all setup pins
	for i in range(1000):
		sp.cbus_write(1)
		time.sleep(0.1)
		sp.cbus_write(2)
		time.sleep(0.1)
		sp.cbus_write(4)
		time.sleep(0.1)
		sp.cbus_write(8)
		time.sleep(0.1)
	return
	# while True:
	# 	sp.cbus_write(1)
	# 	time.sleep(0.1)
	# 	sp.cbus_write(2)
	# 	time.sleep(0.1)
	# 	sp.cbus_write(4)
	# 	time.sleep(0.1)
	# 	sp.cbus_write(8)
	# 	time.sleep(0.1)
	# break

	# Print the current value of all setup pins
	print("CBUS: %s" % sp.cbus_read())


if __name__ == '__main__':
	main()
