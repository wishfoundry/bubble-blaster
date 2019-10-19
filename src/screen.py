import os
from rpi_backlight import Backlight

# any number from 0 to 255
# /sys/class/backlight/rpi_backlight/brightness

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

isRasperry = os.uname()[4].startswith('arm')

bl = Backlight() if isRasperry else dotdict({'brightness': None })

def brightness(value):
    print("brightness: " + str(value))
    bl.brightness = int(value)