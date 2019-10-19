from rpi_backlight import Backlight

# any number from 0 to 255
# /sys/class/backlight/rpi_backlight/brightness


def brightness(int):
    bl = Backlight()
    bl.brightness(int)