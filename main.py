#/usr/bin/python3
from backpack import *
import sys, time

#Backpack
backpack_address = 0x70

#Initialize Controller for 14 Segment Display
backpack = Segments(SMBus(1), backpack_address, 0b0)

backpack.toggle_power() 
first, second = (0, 0)
while True:
    a = input(str(first) + ' ' + str(second))
    if a == 'c':
        backpack.update('clear')
        first, second = (0, 0)
    elif a == 'j':
        first += -1
        backpack.write_block(0b0, [first])
    elif a == 'k':
        first += 1
        backpack.write_block(0b0, [first])
    elif a == 'l':
        second += -1
        backpack.write_block(0b1, [second])
    elif a == ';':
        second += 1
        backpack.write_block(0b1, [second])
    elif a == 'f':
        new = input('first: ')
        first = int(new)
        backpack.write_block(0b0, [first])
    elif a == 's':
        new = input('second: ')
        second = int(new)
        backpack.write_block(0b1, [second])

backpack.toggle_power() 

