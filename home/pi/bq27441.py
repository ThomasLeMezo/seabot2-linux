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

def get_data():
	# Read Control
	control = bus.read_word_data(DEVICE_ADDRESS, Control_REG)
	time.sleep(0.01)
	#control = ((control >> 8) & 0xFF) | ((control & 0xFF) << 8)  # Swap bytes

	if not ((control >> 7) & 0b1):
		return False

	# Read Temperature
	temperature = bus.read_word_data(DEVICE_ADDRESS, Temperature_REG)
	time.sleep(0.01)
	#temperature = ((temperature >> 8) & 0xFF) | ((temperature & 0xFF) << 8)  # Swap bytes

	# Read the voltage from the fuel gauge
	voltage = bus.read_word_data(DEVICE_ADDRESS, Voltage_REG)
	time.sleep(0.01)
	#voltage = ((voltage >> 8) & 0xFF) | ((voltage & 0xFF) << 8)  # Swap bytes

	# Read Flag
	flag = bus.read_word_data(DEVICE_ADDRESS, Flags_REG)
	time.sleep(0.01)
	#flag = ((flag >> 8) & 0xFF) | ((flag & 0xFF) << 8)  # Swap bytes

	# Read NominalAvailableCapacity
	nominalavailablecapacity = bus.read_word_data(DEVICE_ADDRESS, NominalAvailableCapacity_REG)
	time.sleep(0.01)
	#nominalavailablecapacity = ((nominalavailablecapacity >> 8) & 0xFF) | ((nominalavailablecapacity & 0xFF) << 8)  # Swap bytes

	# Read FullAvailableCapacity
	fullavailablecapacity = bus.read_word_data(DEVICE_ADDRESS, FullAvailableCapacity_REG)
	time.sleep(0.01)
	#fullavailablecapacity = ((fullavailablecapacity >> 8) & 0xFF) | ((fullavailablecapacity & 0xFF) << 8)  # Swap bytes

	# Read RemainingCapacity
	remainingcapacity = bus.read_word_data(DEVICE_ADDRESS, RemainingCapacity_REG)
	time.sleep(0.01)
	#remainingcapacity = ((remainingcapacity >> 8) & 0xFF) | ((remainingcapacity & 0xFF) << 8)  # Swap bytes

	# Read FullChargeCapacity
	fullchargecapacity = bus.read_word_data(DEVICE_ADDRESS, FullChargeCapacity_REG)
	time.sleep(0.01)
	#fullchargecapacity = ((fullchargecapacity >> 8) & 0xFF) | ((fullchargecapacity & 0xFF) << 8)  # Swap bytes

	# Read AverageCurrent
	averagecurrent = ctypes.c_int16(bus.read_word_data(DEVICE_ADDRESS, AverageCurrent_REG)).value
	time.sleep(0.01)
	#averagecurrent = ((averagecurrent >> 8) & 0xFF) | ((averagecurrent & 0xFF) << 8)  # Swap bytes

	# Read StandbyCurrent
	standbycurrent = ctypes.c_int16(bus.read_word_data(DEVICE_ADDRESS, StandbyCurrent_REG)).value
	time.sleep(0.01)
	#standbycurrent = ((standbycurrent >> 8) & 0xFF) | ((standbycurrent & 0xFF) << 8)  # Swap bytes

	# Read MaxLoadCurrent
	maxloadcurrent = ctypes.c_int16(bus.read_word_data(DEVICE_ADDRESS, MaxLoadCurrent_REG)).value
	time.sleep(0.01)
	#maxloadcurrent = ((maxloadcurrent >> 8) & 0xFF) | ((maxloadcurrent & 0xFF) << 8)  # Swap bytes

	# Read AveragePower
	averagepower = ctypes.c_int16(bus.read_word_data(DEVICE_ADDRESS, AveragePower_REG)).value
	time.sleep(0.01)
	#averagepower = ((averagepower >> 8) & 0xFF) | ((averagepower & 0xFF) << 8)  # Swap bytes

	# Read StateOfCharge
	stateofcharge = bus.read_word_data(DEVICE_ADDRESS, StateOfCharge_REG)
	time.sleep(0.01)
	#stateofcharge = ((stateofcharge >> 8) & 0xFF) | ((stateofcharge & 0xFF) << 8)  # Swap bytes

	# Read InternalTemperature
	internaltemperature = bus.read_word_data(DEVICE_ADDRESS, InternalTemperature_REG)
	time.sleep(0.01)
	#internaltemperature = ((internaltemperature >> 8) & 0xFF) | ((internaltemperature & 0xFF) << 8)  # Swap bytes

	# Read StateOfHealth
	stateofhealth = bus.read_word_data(DEVICE_ADDRESS, StateOfHealth_REG)
	time.sleep(0.01)
	stateofhealth_status = stateofhealth >> 8
	stateofhealth_percent = stateofhealth & 0xFF
	#stateofhealth = ((stateofhealth >> 8) & 0xFF) | ((stateofhealth & 0xFF) << 8)  # Swap bytes

	# Read RemainingCapacityUnfiltered
	remainingcapacityunfiltered = bus.read_word_data(DEVICE_ADDRESS, RemainingCapacityUnfiltered_REG)
	time.sleep(0.01)
	#remainingcapacityunfiltered = ((remainingcapacityunfiltered >> 8) & 0xFF) | ((remainingcapacityunfiltered & 0xFF) << 8)  # Swap bytes

	# Read RemainingCapacityFiltered
	remainingcapacityfiltered = bus.read_word_data(DEVICE_ADDRESS, RemainingCapacityFiltered_REG)
	time.sleep(0.01)
	#remainingcapacityfiltered = ((remainingcapacityfiltered >> 8) & 0xFF) | ((remainingcapacityfiltered & 0xFF) << 8)  # Swap bytes

	# Read FullChargeCapacityUnfiltered
	fullchargecapacityunfiltered = bus.read_word_data(DEVICE_ADDRESS, FullChargeCapacityUnfiltered_REG)
	time.sleep(0.01)
	#fullchargecapacityunfiltered = ((fullchargecapacityunfiltered >> 8) & 0xFF) | ((fullchargecapacityunfiltered & 0xFF) << 8)  # Swap bytes

	# Read FullChargeCapacityFiltered
	fullchargecapacityfiltered = bus.read_word_data(DEVICE_ADDRESS, FullChargeCapacityFiltered_REG)
	time.sleep(0.01)
	#fullchargecapacityfiltered = ((fullchargecapacityfiltered >> 8) & 0xFF) | ((fullchargecapacityfiltered & 0xFF) << 8)  # Swap bytes

	# Read StateOfChargeUnfiltered
	stateofchargeunfiltered = bus.read_word_data(DEVICE_ADDRESS, StateOfChargeUnfiltered_REG)
	time.sleep(0.01)
	#stateofchargeunfiltered = ((stateofchargeunfiltered >> 8) & 0xFF) | ((stateofchargeunfiltered & 0xFF) << 8)  # Swap bytes

	# Read TrueRemainingCapacity
	trueremainingcapacity = bus.read_word_data(DEVICE_ADDRESS, TrueRemainingCapacity_REG)
	time.sleep(0.01)
	#trueremainingcapacity = ((trueremainingcapacity >> 8) & 0xFF) | ((trueremainingcapacity & 0xFF) << 8)  # Swap bytes

	# Print values
	print("Control: 0x{0:04X}".format(control))
	print(" SHUTDOWNEN = \t", (control >> 15)&0b1)
	print(" WDRESET = \t", (control >> 14)&0b1)
	print(" SS = \t\t", (control >> 13)&0b1)
	print(" CALMODE = \t", (control >> 12)&0b1)
	print(" CCA = \t\t", (control >> 11)&0b1)
	print(" BCA = \t\t", (control >> 10)&0b1)
	print(" QMAX_UP = \t", (control >> 9)&0b1)
	print(" RES_UP = \t", (control >> 8)& 0b1)
	print(" INITCOMP = \t", (control >> 7) & 0b1)
	print(" HIBERNATE = \t", (control >> 6) & 0b1)
	print(" RSVD = \t", (control >> 5) & 0b1)
	print(" SLEEP = \t", (control >> 4) & 0b1)
	print(" LDMD = \t", (control >> 3) & 0b1)
	print(" RUP_DIS = \t", (control >> 2) & 0b1)
	print(" VOK = \t\t", (control >> 1) & 0b1)
	print(" RSVD = \t", (control >> 0) & 0b1)

	print("Temperature: {0:.2f} C".format(temperature/10.0-273.15))
	print("Voltage: {0:.2f} V".format(voltage/1000.0))
	print("Flag: 0x{0:04X}".format(flag))
	print("NominalAvailableCapacity: {0:d} mAh".format(nominalavailablecapacity))
	print("FullAvailableCapacity: {0:d} mAh".format(fullavailablecapacity))
	print("RemainingCapacity: {0:d} mAh".format(remainingcapacity))
	print("FullChargeCapacity: {0:d} mAh".format(fullchargecapacity))
	print("AverageCurrent: {0:d} mA".format(averagecurrent))
	print("StandbyCurrent: {0:d} mA".format(standbycurrent))
	print("MaxLoadCurrent: {0:d} mA".format(maxloadcurrent))
	print("AveragePower: {0:d} mW".format(averagepower))
	print("StateOfCharge: {0:d} %".format(stateofcharge))
	print("InternalTemperature: {0:.2f} C".format(internaltemperature/10.0-273.15))
	print("StateOfHealth_status: {0:d}".format(stateofhealth_status))
	print("StateOfHealth_percent: {0:d} %".format(stateofhealth_percent))
	print("RemainingCapacityUnfiltered: {0:d} mAh".format(remainingcapacityunfiltered))
	print("RemainingCapacityFiltered: {0:d} mAh".format(remainingcapacityfiltered))
	print("FullChargeCapacityUnfiltered: {0:d} mAh".format(fullchargecapacityunfiltered))
	print("FullChargeCapacityFiltered: {0:d} mAh".format(fullchargecapacityfiltered))
	print("StateOfChargeUnfiltered: {0:d} %".format(stateofchargeunfiltered))
	print("TrueRemainingCapacity: {0:d} mAh".format(trueremainingcapacity))

	return True


while(not get_data()):
	time.sleep(0.5)


