from RPi.GPIO import *

#Object Controls LEDs in a Line Configuration
class LightLine:
    def __init__(self, *pins):
        self.lights = pins
        self.activated = 0 #Selects which light is on
        self.on = False
        setwarnings(False)
        for pin in self.lights:
            setup(pin, OUT)

    def toggle_power(self):
        if self.on:
            for pin in self.lights:
                output(pin, LOW)
            self.on = False
        else:
            output(self.lights[self.activated], HIGH)

    def update(self):
        self.activated += 1 
        if self.activated == len(self.lights):
            self.activated = 0 
        if self.on:
            # Temporarily Turns off Display
            self.toggle_power()
            # Turns display back on with new light
            self.toggle_power()

    def __str__(self):
        return 'Lightline: Pins %s' % str(self.lights)

