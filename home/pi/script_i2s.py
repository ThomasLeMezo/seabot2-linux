
i2cset -y 1 0x4E 0x02 0x81 # Wake up
i2cset -y 1 0x4E 0x01 0x01 # Reset
sleep 0.1
i2cset -y 1 0x4E 0x00 0x00 # Select page 0
i2cset -y 1 0x4E 0x02 0x81 # Wake up

sleep 0.1
i2cset -y 1 0x4E 0x07 0x70 # I2S - 32 bit
#i2cset -y 1 0x4E 0x07 0x80 # I2S - 20 bit
i2cset -y 1 0x4E 0x73 0x80 # Enable CH1 input
i2cset -y 1 0x4E 0x74 0x80 # Enable ASI output CH1
i2cset -y 1 0x4E 0x75 0x60 # Power up adc & pll


#   0 bcm2835 Headphones: - (hw:0,0), ALSA (0 in, 8 out)
#   1 snd_rpi_i2s_card: simple-card_codec_link snd-soc-dummy-dai-0 (hw:1,0), ALSA (2 in, 2 out)
#   2 sysdefault, ALSA (0 in, 128 out)
#   3 samplerate, ALSA (0 in, 128 out)
#   4 speexrate, ALSA (0 in, 128 out)
#   5 pulse, ALSA (32 in, 32 out)
#   6 upmix, ALSA (0 in, 8 out)
#   7 vdownmix, ALSA (0 in, 6 out)
#   8 dmix, ALSA (0 in, 2 out)
# * 9 default, ALSA (32 in, 32 out)
