
i2cset -y 1 0x4E 0x02 0x81 # Wake up
i2cset -y 1 0x4E 0x01 0x01 # Reset
sleep 0.1
i2cset -y 1 0x4E 0x00 0x00 # Select page 0
i2cset -y 1 0x4E 0x02 0x81 # Wake up

sleep 0.1
#i2cset -y 1 0x4E 0x07 0x70 # I2S - 32 bit
i2cset -y 1 0x4E 0x07 0x60 # I2S - 24 bit
#i2cset -y 1 0x4E 0x07 0x80 # I2S - 20 bit
i2cset -y 1 0x4E 0x73 0x80 # Enable CH1 input
i2cset -y 1 0x4E 0x74 0x80 # Enable ASI output CH1
i2cset -y 1 0x4E 0x75 0x60 # Power up adc & pll
