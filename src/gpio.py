import importlib.util
from PySide2.QtCore import Slot, Property, Signal, QObject, QTimer
from config import POST_PRIME_DELAY, PRIME_DURATION, CLEAN_CYCLE_TIME, RINSE_CYCLE_TIME
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

TIMERS = []

def _removeTimer(tmr):
    TIMERS.remove(tmr)
def _runTimer(tmr, fun):
    _removeTimer(tmr)
    fun()
    print('ran io timer')

def timer(ms, fun):
    tmr = QTimer()
    tmr.setSingleShot(True)
    tmr.timeout.connect(lambda : _runTimer(tmr, fun))
    TIMERS.append(tmr)
    tmr.start(ms)

def clearTimers():
    while TIMERS:
        tmr = TIMERS.pop()
        tmr.stop()

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

def turnOffAll(pins):
    for pin in pins:
        turnOff(pin)

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


def mainCycle(duration):
    print("running main cycle")
    clearTimers()
    turnOn(PRIME)
    timer(PRIME_DURATION, lambda : turnOff(PRIME))
    timer(POST_PRIME_DELAY, lambda : turnOnAll([MAIN, OXY, ELECTRO]))
    timer(duration, lambda : turnOffAll([MAIN, OXY, ELECTRO]))

def rinseCycle():
    #  drop
    print("running rinse cycle")
    turnOnAll([PRIME, MAIN])
    timer(45 * 1000, lambda : turnOn(OXY))
    timer(RINSE_CYCLE_TIME * 60 * 1000, lambda : turnOffAll(PINS))

def cleanCycle():
    # broom/car-turbo-charger
    print("running clean cycle")
    turnOnAll([MAIN, PRIME, OXY])
    timer(CLEAN_CYCLE_TIME * 60 * 1000, lambda : turnOffAll(PINS))

def runCycle(duration):
    if duration == (CLEAN_CYCLE_TIME * 60 * 1000):
        cleanCycle()
    elif duration == (RINSE_CYCLE_TIME * 60 * 1000):
        rinseCycle()
    else:
        mainCycle(duration)

def stopCycle():
    print('stopping cycle')
    turnOffAll(PINS)
    clearTimers()