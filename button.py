from smbus import *
from RPi.GPIO import *

#Button Object
class Button:
    def __init__(self, input_pin):
        setmode(BOARD)
        setup(input_pin, IN)
        self.input_pin = input_pin

    def press(self):
        if input(input_pin) == 1:
            return True
        else:
            return False

    def __str__(self):
        represent = 'Button: Pin %s, ' % str(self.input_pin)
        represent += 'Activated' if self.press else 'Deactivated'
        return represent
