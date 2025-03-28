#!/usr/bin/zsh

# Pass code
i2cset -y 1 0x55 0x00 0x00 0x80 i
i2cset -y 1 0x55 0x00 0x00 0x80 i

# Set CFGUPDATE
i2cset -y 1 0x55 0x00 0x13 0x00 i

# Control CFGUPDATE
i2cget -y 1 0x55 0x06

i2cset -y 1 0x55 0x61 0x00
i2cset -y 1 0x55 0x3E 0x52
i2cset -y 1 0x55 0x3F 0x00

# old Checksum
echo "Old Checksum"
i2cget -y 1 0x55 0x60

# Old value
echo "Old Value Capacity (0x03 0xE8)"
i2cget -y 1 0x55 0x4A
i2cget -y 1 0x55 0x4B

# Write new value
echo "Write new values (0x14 0x50)"
i2cset -y 1 0x55 0x4A 0x14
i2cset -y 1 0x55 0x4B 0x50

# Write checksum
echo "Write checksum"
i2cset -y 1 0x55 0x60 0x6F

# Check values
echo "Check values"
i2cget -y 1 0x55 0x4A
i2cget -y 1 0x55 0x4B
# i2cget -y 1 0x55 0x60

# exit CFGUPDATE
echo "exit config"
i2cset -y 1 0x55 0x00 0x42 0x00 i

# Control CFGUPDATE
echo "Control CFGUPDATE"
i2cget -y 1 0x55 0x06

# # Sealed
# echo "Seal"
# i2cset -y 1 0x55 0x00 0x20 0x00 i

# # Control CFGUPDATE
# sleep 5
# echo "Control CFGUPDATE"
# sleep 2
# i2cget -y 1 0x55 0x06

# for i in {1..30}
# do
#    echo "i = $i"
#    i2cget -y 1 0x55 0x0A w
#    sleep 1
# done