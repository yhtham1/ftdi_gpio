#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ft232
import time



#cusb bit0: NRST
#cusb bit1: BOOT0
#cusb bit2: BOOT1
#cusb bit3: PB14

# n:0 NORMAL BOOT
# n:1 BOOT LOADER
# n:2 not use
# n:3 RAM BOOT

def reboot(sp, n):
	pat = int(n * 2)
	sp.cbus_setup(mask=0x0f, init=pat)
	sp.cbus_write(pat)
	time.sleep(0.1)
	sp.cbus_setup(mask=0x0e, init=pat)

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
	reboot(sp, 3)
	return

if __name__ == '__main__':
	main()
