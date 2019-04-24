from RPi.GPIO import *

#Object Controls LEDs in a Line Configuration
class LightLine:
    def __init__(self, pins):
        self.lights = pins
        self.activated = 0 #Selects which light is on
        setwarnings(False)
        self.on = False
        for pin in self.lights:
            setup(pin, OUT)
            output(pin, LOW)

    def toggle_power(self, force = 'actionless'):
        if self.on or force.lower() == 'off':
            for pin in self.lights:
                output(pin, LOW)
            self.on = False
        else:
            output(self.lights[self.activated], HIGH)

    def update(self):
        self.activated += 1 
        if self.activated == len(self.lights):
            self.activated = 0 
        # Temporarily Turns off Display
        for pin in self.lights:
            output(pin, LOW)
        # Turns display back on with new light
        output(self.lights[self.activated], HIGH)

    def __str__(self):
        return 'Lightline: Pins %s' % str(self.lights)

