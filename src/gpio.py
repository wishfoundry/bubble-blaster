import importlib.util
from PySide2.QtCore import Slot, Property, Signal, QObject, QTimer
from config import POST_PRIME_DELAY, PRIME_DURATION
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

PINS = [4,22,6,26]
RELAY1, RELAY2, RELAY3, RELAY4 = PINS
MAIN = RELAY1
OXY = RELAY2
PRIME = RELAY3
ELECTRO = RELAY4

def setupPin(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def setupPins():
    print('using fake mode on pins: ' + str(isFake))
    GPIO.setmode(GPIO.BCM)
    [setupPin(i) for i in PINS]

def turnOn(pin): GPIO.output(pin, GPIO.HIGH)
def turnOff(pin): GPIO.output(pin, GPIO.LOW)

def cleanup():
    print('cleaning up pins')
    GPIO.cleanup()

def turnOnAll(pins):
    for pin in pins:
        turnOn(pin)

def testRelays():
    print('testing relays')
    # interval = 400
    # QTimer.singleShot(1 * interval, lambda : turnOn(B))
    # QTimer.singleShot(2 * interval, lambda : turnOn(C))
    # QTimer.singleShot(3 * interval, lambda : turnOn(D))
    # QTimer.singleShot(4 * interval, lambda : turnOff(A))
    # QTimer.singleShot(5 * interval, lambda : turnOff(B))
    # QTimer.singleShot(6 * interval, lambda : turnOff(C))
    # QTimer.singleShot(7 * interval, lambda : turnOff(D))


def runCycle(duration):
    print("running cycle")
    turnOn(PRIME)
    QTimer.singleShot(PRIME_DURATION, lambda : turnOff(PRIME))
    QTimer.singleShot(POST_PRIME_DELAY, lambda : turnOnAll([MAIN, OXY, ELECTRO]))
    QTimer.singleShot(duration, lambda : turnOnAll([MAIN, OXY, ELECTRO]))

def stopCycle():
    print('stopping cycle')
    for pin in PINS:
        turnOff(pin)