from math import *

#fRef = 1000000
fRef = 3686400
#baudrate = 9600.0
baudrate = 38400.0
D = fRef/(16.0*baudrate)
DIV = floor(D)# 6 ?

FRACT = round(16.0 * (D-DIV)) # 8

print(DIV, FRACT)

DACTUAL = DIV + FRACT/16
BR = fRef/(16*DACTUAL)

print(BR)
