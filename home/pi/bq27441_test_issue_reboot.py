import smbus
import ctypes
import time

# I2C address of the bq27441 fuel gauge
DEVICE_ADDRESS = 0x55

Control_REG = 0x00
Temperature_REG = 0x02
Voltage_REG = 0x04
Flags_REG = 0x06
NominalAvailableCapacity_REG = 0x08
FullAvailableCapacity_REG = 0x0A
RemainingCapacity_REG = 0x0C
FullChargeCapacity_REG = 0x0E
AverageCurrent_REG = 0x10
StandbyCurrent_REG = 0x12
MaxLoadCurrent_REG = 0x14
AveragePower_REG = 0x18
StateOfCharge_REG = 0x1C
InternalTemperature_REG = 0x1E
StateOfHealth_REG = 0x20
RemainingCapacityUnfiltered_REG = 0x28
RemainingCapacityFiltered_REG = 0x2A
FullChargeCapacityUnfiltered_REG = 0x2C
FullChargeCapacityFiltered_REG = 0x2E
StateOfChargeUnfiltered_REG = 0x30
TrueRemainingCapacity_REG = 0x6A

# Initialize the I2C bus
bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi boards
time.sleep(0.5)

def get_control():
	# Read Control
	control = bus.read_word_data(DEVICE_ADDRESS, Control_REG)
	#control = ((control >> 8) & 0xFF) | ((control & 0xFF) << 8)  # Swap bytes

	# Print values
	# print("Control: 0x{0:04X}".format(control))
	# print(" SHUTDOWNEN = ", (control >> 15)&0b1)
	# print(" WDRESET = ", (control >> 14)&0b1)
	# print(" SS = ", (control >> 13)&0b1)
	# print(" CALMODE = ", (control >> 12)&0b1)
	# print(" CCA = ", (control >> 11)&0b1)
	# print(" BCA = ", (control >> 10)&0b1)
	# print(" QMAX_UP = ", (control >> 9)&0b1)
	# print(" RES_UP = ", (control >> 8)& 0b1)
	print(" INITCOMP = ", (control >> 7) & 0b1)
	# print(" HIBERNATE = ", (control >> 6) & 0b1)
	# print(" RSVD = ", (control >> 5) & 0b1)
	# print(" SLEEP = ", (control >> 4) & 0b1)
	# print(" LDMD = ", (control >> 3) & 0b1)
	# print(" RUP_DIS = ", (control >> 2) & 0b1)
	# print(" VOK = ", (control >> 1) & 0b1)
	# print(" RSVD = ", (control >> 0) & 0b1)

for i in range(200):
	get_control()
	time.sleep(0.1)



