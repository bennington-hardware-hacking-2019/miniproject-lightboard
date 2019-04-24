import components.button, components.lightline, components.backpack
import sys, time

class Column:
    def __init__(self, bus, segment_address, characters,
     button_pin, lightline_pins):
        self.segment = components.backpack.Segment(bus, 
         segment_address, characters)
        self.switch = components.button.Button(button_pin)
        self.mood_lights = components.lightline.LightLine(lightline_pins)
        self.segment.toggle_power()
        self.mood_lights.toggle_power()

    def activate(self, name):
        self.segment.update(name)
        while True:
            if self.switch.press(): 
                self.mood_lights.update()
                time.sleep(1)
    
    def off(self):
        if self.segment.on:
            self.segment.toggle_power()
        self.segment.update('clear')
        self.mood_lights.toggle_power('off')
        self.mood_lights.activated = 0

    def __str__(self):
        return 'Column(%s; %s; %s)' % (str(self.segment), str(self.switch),
         str(self.mood_lights))

if __name__ == '__main__':
    column1 = Column(1, 0x71, 16, [31, 35, 37])
    print(column1)
    column1.activate('Five')
