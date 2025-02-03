import smbus
import time
from math import *

BQ25890_I2C_ADDRESS=0x6A

# Initialize the I2C bus
bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi boards

def get_charger_status():
	print("-- REG 0x0B --")
	charger_status = bus.read_byte_data(BQ25890_I2C_ADDRESS, 0x0B)

	VBUS_STAT = (charger_status >> 5) & 0b111
	CHRG_STAT = (charger_status >> 3) & 0b11
	PG_STAT = (charger_status >> 2) & 0b1
	VSYS_STAT = (charger_status & 0b1)

	if(VBUS_STAT == 0b000):
		print('\t', "No Input 001: USB Host SDP")
	elif(VBUS_STAT == 0b010):
		print('\t', "USB CDP (1.5A)")
	elif(VBUS_STAT == 0b011):
		print('\t', "USB DCP (3.25A)")
	elif(VBUS_STAT == 0b100):
		print('\t', "Adjustable High Voltage DCP (MaxCharge) (1.5A)")
	elif(VBUS_STAT == 0b101):
		print('\t', "Unknown Adapter (500mA)")
	elif(VBUS_STAT == 0b110):
		print('\t', "Non-Standard Adapter (1A/2A/2.1A/2.4A)")
	elif(VBUS_STAT == 0b111):
		print('\t', "OTG")

	if(CHRG_STAT == 0b00):
		print('\t', "Not Charging")
	elif(CHRG_STAT == 0b01):
		print('\t', "Pre-charge ( < VBATLOWV)")
	elif(CHRG_STAT == 0b10):
		print('\t', "Fast Charging")
	elif(CHRG_STAT == 0b11):
		print('\t', "Charge Termination Done")

	if(PG_STAT == 0b0):
		print('\t', "Not Power Good")
	elif(PG_STAT == 0b1):
		print('\t', "Power Good")

	if(VSYS_STAT == 0b0):
		print('\t', "Not in VSYSMIN regulation (BAT > VSYSMIN)")
	elif(VSYS_STAT == 0b1):
		print('\t', "In VSYSMIN regulation (BAT < VSYSMIN)")


def adc_measure():
	bus.write_byte_data(BQ25890_I2C_ADDRESS, 0x02, 0x9D)
	time.sleep(1)

def get_battery_voltage():
	print("-- REG 0x0E --")
	batt_status = bus.read_byte_data(BQ25890_I2C_ADDRESS, 0x0E)
	thermal_regulation = (batt_status >> 7)
	adc = (batt_status) & 0x7F

	adc_offset = 2.304
	adc_max = 4.848
	print('\t',"adc ()", (adc/0x7F)*(adc_max-adc_offset)+adc_offset)
	if(thermal_regulation == 0):
		print('\t',"Thermal : Normal")
	else:
		print('\t',"Thermal : In Thermal regulation")

def get_current_limit():
	print("-- REG 0x00 --")
	current_data = bus.read_byte_data(BQ25890_I2C_ADDRESS, 0x00)
	EN_HIZ = (current_data>>7) & 0b1
	EN_ILIM = (current_data>>6) & 0b1
	IINLIM = (current_data & 0x3F)

	print('\t',"EN_HIZ = ", "Enable" if EN_HIZ else "Disable")
	print('\t',"EN_ILIM = ", "Enable" if EN_ILIM else "Disable")
	print('\t',"Input Current limit = ", round(((IINLIM/0x3F)*(3250-100)) + 100), "mA")

def get_current_fast_charge():
	print("-- REG 0x04 --")
	current_fast_data = bus.read_byte_data(BQ25890_I2C_ADDRESS, 0x04)
	ICHG = (current_fast_data & 0x7F)
	EN_PUMPX = (current_fast_data >> 7) & 0b1

	print('\t', "EN_PUMPX = ", "Enable" if EN_PUMPX else "Disable")
	print('\t', "Fast Charge Current Limit = ", round((ICHG/0b1001111)*5056), "mA")

def set_fast_charge_current_limit():
	bus.write_byte_data(BQ25890_I2C_ADDRESS, 0x04, 0x28) # set to 2560mA

get_charger_status()
adc_measure()
get_battery_voltage()
get_current_limit()
#set_fast_charge_current_limit()
get_current_fast_charge()