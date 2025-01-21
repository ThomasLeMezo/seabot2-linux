import time
import spidev

# Create SPI object
spi = spidev.SpiDev()
spi.open(0, 1)  # Specify the SPI bus and device

# Set SPI mode and clock frequency
spi.mode = 0b00  # Mode 0 =? CPOL = 0 and clock phase CPHA = 0
spi.max_speed_hz = 500000  # Set the clock frequency to 1 MHz

# Configure the MAX3107 control register
revid_reg = 0x1F
FIFOTrgLvl = 0x10
TxFIFOLvl = 0x11
RxFIFOLvl = 0x12

FlowCtrl_reg = 0x13
ISR_reg = 0x02
RHR_reg = 0x00
LCR_reg = 0x0B
PLLConfig_reg = 0x1A

CLKSource_reg = 0x1E
DIVLSB_reg = 0x1C
BRGConfig_reg = 0x1B

##### Configure Baudrate

DIV = 6
FRAC = 0 # 8
# Set FRACT

DIVLSB = DIV & 0xFF
BRGConfig = FRAC & 0x1F

CLKSource = 0x18 # external clk

LCR = 0x03
FlowCtrl = 0x3 # 0x03
PLLConfig = 0x6

spi.writebytes([LCR_reg | 0x80, LCR])
spi.writebytes([CLKSource_reg | 0x80, CLKSource])
spi.writebytes([DIVLSB_reg | 0x80, DIVLSB])
spi.writebytes([BRGConfig_reg | 0x80, BRGConfig])
spi.writebytes([FlowCtrl_reg | 0x80, FlowCtrl])
spi.writebytes([PLLConfig_reg | 0x80, PLLConfig])

##### Get all register

# spi.writebytes2([0x00])
# data_msg = spi.readbytes(31)
# for d in range(len(data_msg)):
# 	print(hex(d+1), hex(data_msg[d]))

def read_all_register():
	print("Read Register")
	arr0 = [0x00] * 32
	arr0[0] = 0x01
	data_msg = spi.xfer2(arr0)
	for d in range(len(data_msg)):
		print(hex(d), hex(data_msg[d]))

read_all_register()

##### Read Data
i=5
while(True):

	# i+=1
	# if i>127 :
	# 	i=5
	# tx_msg = [RHR_reg | 0x80, i] # Transmit (0x00 | 0x80)
	# spi.writebytes(tx_msg)

	data = spi.xfer2([0x1F, 0x00]) # Read (0x00 | 0x80)
	#data = spi.xfer2([RHR_reg, 0x00]) # Read (0x00 | 0x80)
	#print(chr(data[1]), end='')
	print(data)
	time.sleep(0.1)

spi.close()
