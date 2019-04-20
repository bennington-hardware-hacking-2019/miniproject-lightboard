from RPI.GPIO import *

#Object Controls LEDs in a Line Configuration
class LightLine:
    def __init__(self, *pins):
        self.lights = pins
        self.activated = 0 #Selects which light is on
        self.on = False
        setwarnings(False)
        for pin in lights:
            setup(pin, OUT)

    def toggle_power(self):
        if self.on:
            for pin in lights:
                output(pin, LOW)
            self.on = False
        else:
            output(pin[self.counter], HIGH)

    def update(self):
        self.activated += 1 
        if self.activated == len(lights):
            self.activated = 0 
        if self.on:
            # I could have rewritten the code above but this was easier
            self.toggle_power()
            self.toggle_power()
            

        
