import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
    isFake = False
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
	
    import FakeRPi.GPIO as GPIO
    isFake = True

A = 4
B = 22
C = 6
D = 26
PINS = [A,B,C,D]

def setupPin(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def setupPins():
    print('using fake mode on pins: ' + str(isFake))
    GPIO.setmode(GPIO.BCM)
    setupPin(A)
    setupPin(D)
    setupPin(C)
    setupPin(D)

def turnOn(pin): GPIO.output(A, GPIO.HIGH)
def turnOff(pin): GPIO.output(A, GPIO.LOW)

def cleanup():
    print('cleaning up pins')
    GPIO.cleanup()