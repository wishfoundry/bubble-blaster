import math
import datetime
from PySide2.QtGui import *
from PySide2.QtCore import Slot, Property, Signal, QObject, QTimer
from PySide2.QtGui import QGuiApplication, QKeySequence
import gpio as Gpio
import screen as Screen
import config


def minutesOf(ms):
    return math.floor(ms / 60000)

def secondsOf(ms):
    # ((millis % 60000) / 1000).toFixed(0);
    return math.floor((ms / 1000) % 60)

def toDisplayTime(min, sec):
    return str(min).zfill(2) + ":" + str(sec).zfill(2)

def msToDisplayTime(ms):
    return toDisplayTime(minutesOf(ms), secondsOf(ms))


class Controller(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        Gpio.setupPins()
        # 10 minutes default
        self._ms = 10 * 60 * 1000
        self._isRunning = False
        self._tickTimer = QTimer(self)
        self._timer = QTimer(self)
        self._tickTimer.timeout.connect(self.onTick)
        self._timer.timeout.connect(self.onTimeout)
        self.destroyed.connect(lambda : Gpio.cleanup())

    @Signal
    def notifyIsRunning(self): pass

    @Property(bool, notify=notifyIsRunning)
    def isRunning(self):
        return self._isRunning

    @isRunning.setter
    def setIsRunning(self, value):
        self._isRunning = value
    
    @Slot()
    def quit(self):
        print('manually killing app')
        QGuiApplication.quit()

    @Slot(str)
    def log(self, msg):
        print(msg)

    @Slot()
    def toggle(self):
        if self._isRunning:
            self.stop()
        else:
            self.start()

    def start(self):
        print("started")
        self._timer.start(self._ms)
        self._tickTimer.start(1000)
        self._isRunning = True
        self.notifyIsRunning.emit()
        Gpio.runCycle(self._ms)
    
    def onTimeout(self):
        self.stop()
    
    def onTick(self):
        self.displayTimeChanged.emit()
    

    def stop(self):
        print("stopped")
        self._tickTimer.stop()
        self._timer.stop()
        self._isRunning = False
        self.displayTimeChanged.emit()
        self.notifyIsRunning.emit()
        Gpio.stopCycle()


    @Signal
    def displayTimeChanged(self): pass

    @Property(str, notify=displayTimeChanged)
    def displayTime(self):
        return msToDisplayTime(self._ms if not self._isRunning else self._timer.remainingTime())
    
    @Signal
    def minuteChanged(self): pass

    @Property(int, notify=minuteChanged)
    def minute(self):
        return minutesOf(self._ms)


    @minute.setter
    def setMinute(self, min):
        if self._isRunning: return
        ms = min * 60 * 1000
        if self._ms == ms: return
        self._ms = ms
        self.minuteChanged.emit()
        self.displayTimeChanged.emit()

    # int between 0 and 100
    @Slot(int)
    def brightness(self, value):
        Screen.brightness(value)

    @Property(int)
    def MIN_TIME():
        return config.MIN_TIME
    
    @Property(int)
    def MAX_TIME():
        return config.MAX_TIME