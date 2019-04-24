#!/usr/bin/python3
from backpack import *
import sys, time

#Backpack
backpack_address = 0x71

#Initialize Controller for 14 Segment Display
backpack = Segment(SMBus(1), backpack_address)

backpack.toggle_power() 
first, second = (0, 0)

backpack.update('FiVe')
time.sleep(2)
backpack.update('clear')

backpack.toggle_power() 

