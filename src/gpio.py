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

A = 6
B = 3
C = 22
D = 25

def setupPins():
    print('using fake mode on pins: ' + str(isFake))
    GPIO.setmode(GPIO.BCM)
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setup(A, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    GPIO.setup(C, GPIO.OUT)
    GPIO.setup(D, GPIO.OUT)

def turnOn(pin): GPIO.output(4, GPIO.HIGH)
def turnOff(pin): GPIO.output(4, GPIO.LOW)

def cleanup():
    GPIO.cleanup()