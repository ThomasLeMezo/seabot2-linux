#!/bin/python3

from brping import Ping1D
myPing = Ping1D()
myPing.connect_serial("/dev/ping1D", 115200)
myPing.initialize()
