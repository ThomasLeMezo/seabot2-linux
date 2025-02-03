# Prepare system for emission

# Commmute multiplexer to DAC
# i2c adress of multiplexer ADG729: 0x44
# reset all switch to 0
i2cset -y 1 0x44 0x00
sleep 0.1
# put S2A (S2) and S2B (S6) to 1: 0001 0001 ->
i2cset -y 1 0x44 0x22
sleep 0.1


# Switch relais hydro
i2cset -y 0 0x1A 0xA0 0x01
