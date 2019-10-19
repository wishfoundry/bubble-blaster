import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
	
    import FakeRPi.GPIO as GPIO

A = 7
B = 3
C = 22
D = 25

def setupPins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    GPIO.setup(C, GPIO.OUT)
    GPIO.setup(D, GPIO.OUT)

def turnOn(pin): GPIO.output(pin, GPIO.HIGH)
def turnOff(pin): GPIO.output(pin, GPIO.LOW)

def cleanup():
    GPIO.cleanup()