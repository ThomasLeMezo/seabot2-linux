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

