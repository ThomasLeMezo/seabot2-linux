import smbus
import time
import ctypes
import sys

bus = smbus.SMBus(1)


def set_mode(mode):
	data = bus.write_byte_data(0x1E, 0x05, int(mode))


if(len(sys.argv)>1):
	print(sys.argv[1])
	set_mode(sys.argv[1])