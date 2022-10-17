import smbus
import time
import ctypes
import sys

bus = smbus.SMBus(1)

def set_velocity_Kp(coeff):
	print(coeff)
	coeff = int(round(coeff))
	data = bus.write_word_data(0x1E, 0x60, coeff)

def set_velocity_Ki(coeff):
	print(coeff)
	coeff = int(round(coeff))
	data = bus.write_word_data(0x1E, 0x62, coeff)

def set_velocity_Kd(coeff):
	print(coeff)
	coeff = int(round(coeff))
	data = bus.write_word_data(0x1E, 0x64, coeff)

def set_position_Kp(coeff):
	print(coeff)
	coeff = int(round(coeff))
	data = bus.write_word_data(0x1E, 0x66, coeff)

def set_position_Ki(coeff):
	print(coeff)
	coeff = int(round(coeff))
	data = bus.write_word_data(0x1E, 0x68, coeff)

def set_position_Kd(coeff):
	print(coeff)
	coeff = int(round(coeff))
	data = bus.write_word_data(0x1E, 0x6A, coeff)


if(len(sys.argv)>1):
	set_velocity_Kp(float(sys.argv[1]))
if(len(sys.argv)>2):	
	set_velocity_Ki(float(sys.argv[2]))
if(len(sys.argv)>3):
	set_velocity_Kd(float(sys.argv[3]))

if(len(sys.argv)>4):
	set_position_Kp(float(sys.argv[4]))
if(len(sys.argv)>5):	
	set_position_Ki(float(sys.argv[5]))
if(len(sys.argv)>6):
	set_position_Kd(float(sys.argv[6]))