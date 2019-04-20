#/usr/bin/python3
#14 Segment LED Backpack Controller Object

from smbus import *

class Segments:
    def __init__(self, bus, address, modifier):
        self.bus = bus
        self.address = address
        self.modifier = modifier
        self.on = False

        #System Setup
        self.bus.write_byte(self.address, 0b00100001)

    def write_block(self, cmd, parameters):
        self.bus.write_i2c_block_data(self.address, 
         cmd, parameters)

    #Toggles Power to the Display
    def toggle_power(self): 
        if self.on:
            self.bus.write_byte(self.address, 0b10000000)
        else:
            self.bus.write_byte(self.address, 0b10000001)

    def update(self, name):
        cells = [(0b0, 0b1), (0b10, 0b11), 
         (0b100, 0b101), (0b110, 0b111)]
        num = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 0]
        if name == 'clear':
            for cell in range(16):
                self.write_block(cell, [0])
        else:
            name = str(name)
            while len(name) < 4:
                name = name + ' '
            iter = 0
            for char in name:
                retrieve = 10
                try: 
                   retrieve = int(char) 
                except:
                    pass
                self.write_block(cells[iter], [num[retrieve]])
                iter += 1

#    def __str__(self):

