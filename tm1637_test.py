# MicroPython TM1637 quad 7-segment LED display driver examples
# P8 ------------- CLK
# P13 ------------ DIO
# 3V3 ------------ VCC
# G -------------- GND

import tm1637
from  microbit import *
tm = tm1637.TM1637(clk=pin8, dio=pin13)

# 0-9
_SEGMENTS = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F')
# all LEDS off
tm.write([0, 0, 0, 0])
tm.show('    ')

# display "12__"
tm.number(12)
sleep(1000)

# display "-12.3"
tm.number(-12.3)
sleep(1000)

# display "0123."
tm.write([_SEGMENTS[0],_SEGMENTS[1], _SEGMENTS[2], _SEGMENTS[3]|0x80])
sleep(1000)

counter = 0
while True:
    counter += 1
    tm.show("%4d" % counter)
    sleep(250)

