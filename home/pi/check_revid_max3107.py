import time
import spidev

# Create SPI object
spi = spidev.SpiDev()
spi.open(0, 1)  # Specify the SPI bus and device

# Set SPI mode and clock frequency
spi.mode = 0b01  # Mode 1 (CPOL=0, CPHA=1)
spi.max_speed_hz = 1000000  # Set the clock frequency to 1 MHz

# Configure the MAX3107 control register
revid_reg = 0x1F

# Construct the SPI message to read the RevID register
tx_msg = [revid_reg, 0x00]  # Send control register address followed by a dummy byte

# Perform SPI transfer
rx_msg = spi.xfer2(tx_msg)

# Extract the RevID value from the received message
revid = rx_msg[1]

# Print the RevID
print(f"RevID: 0x{revid:02X}")


arr0 = [0x00] * 31
arr0[0] = 0x01

data_msg = spi.xfer2(arr0)
print(data_msg)

# Close the SPI connection
spi.close()
