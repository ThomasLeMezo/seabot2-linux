#####################################################
# Iridium DTR (Active low)
echo "23" > /sys/class/gpio/export
sleep 0.1
echo "out" > /sys/class/gpio/gpio23/direction
echo "0" > /sys/class/gpio/gpio23/value

# Power On Iridium (Active high)
echo "22" > /sys/class/gpio/export
sleep 0.1
echo "out" > /sys/class/gpio/gpio22/direction
echo "1" > /sys/class/gpio/gpio22/value

gpioset --mode=signal gpiochip0 25=0

#####################################################
# ADC: TLV320ADC6120 (TI) - ADC adress: 0x4E
i2cset -y 0 0x4E 0x02 0x81 # Wake up device and enable AREG
i2cset -y 0 0x4E 0x01 0x01 # Reset software

sleep .1
i2cset -y 0 0x4E 0x00 0x00 # Select page 0
i2cset -y 0 0x4E 0x02 0x81 # Wake up device and enable AREG

sleep .01
i2cset -y 0 0x4E 0x07 0x70 # Set I2S - 32 bit

# Set each channel to corresponding ASI left/right slot
i2cset -y 0 0x4E 0x0B 0x00 #Set Ch-1 data to ASI left slot 0
i2cset -y 0 0x4E 0x0C 0x20 #Set Ch-2 data to ASI right slot 0

# Enable Channels
i2cset -y 0 0x4E 0x73 0xC0 #Enable input Ch-1 and Ch-2
i2cset -y 0 0x4E 0x74 0xC0 # Enable ASI Output Ch-1 and Ch-2 slots

# Channels parmaters (Mic input, differential output, input impedance 20 kOmhs)
i2cset -y 0 0x4E 0x3C 0x08 # Set Channel 1 input type (Mic=08,Line=88) + input impedance 20 kOhms
i2cset -y 0 0x4E 0x41 0x08 # Set Channel 2 input type (Mic=08,Line=88) + input impedance 20 kOhms

#i2cset -y 0 0x4E 0x3C 0x48 # Set Channel 1 input type (Mic=48,Line=C8) + single-ended output
#i2cset -y 0 0x4E 0x41 0x48 # Set Channel 2 input type (Mic=48,Line=C8) + single-ended output

# Set gain to each channel
# gain values: 0dB=0x00, 10dB=0x28, 20dB=0x50, 30dB=78, 40dB=A0 
# (from 0 to 42 dB with 0.5 step -> from 0000 000(0) to 1010 100(0) [first bit (0) for gain sign])
i2cset -y 0 0x4E 0x3D 0x00 # Channel 1 gain set to 0 dB
i2cset -y 0 0x4E 0x42 0x00 # Channel 2 gain set to 0 dB (to do before powering up the ADC!)

# Power-up ADC, MICBIAS and PLL
i2cset -y 0 0x4E 0x75 0xE0
# at this point  FSYNC RATE and RATIO should be set up (see ASI_STS)

#####################################################

#dtoverlay max3107


