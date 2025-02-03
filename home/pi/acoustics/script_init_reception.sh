# Script to commute pcm_clk and pcm_fs in ADG729
# i2c adress of ADG729: 0x44

# reset all switch to 0
i2cset -y 1 0x44 0x00
sleep 0.1

# put S1A (S1) and S1B (S5) to 1: 0001 0001 ->
i2cset -y 1 0x44 0x11
sleep 0.1
