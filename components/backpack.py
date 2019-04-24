#14 Segment LED Backpack Controller Object

from smbus import *

class Segment:
    def __init__(self, bus, address, character_list):
        self.bus = SMBus(bus)
        self.address = address
        self.on = False

        #Load Character Configuration
        self.characters = character_list
                
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
        name = str(name).upper()
        cells = [(0b0, 0b1), (0b10, 0b11), 
         (0b100, 0b101), (0b110, 0b111)]
        if len(name) > 4:
            for cell in range(16):
                self.write_block(cell, [0])
        else:
            while len(name) < 4:
                name = name + ' '
            cell_index = 0
            for char in name:
                self.write_block(cells[cell_index][0], 
                 [self.characters[char][0]])
                self.write_block(cells[cell_index][1], 
                 [self.characters[char][1]])
                cell_index += 1

    def __str__(self):
        return 'Segment Display:  Address %s' % self.address

