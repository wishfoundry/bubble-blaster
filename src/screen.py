from rpi_backlight import Backlight

# any number from 0 to 255
# /sys/class/backlight/rpi_backlight/brightness

bl = Backlight()

def brightness(value):
    print("brightness: " + value)
    bl.brightness = int(value)