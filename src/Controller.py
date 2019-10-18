from PySide2.QtGui import *
from PySide2.QtCore import Slot, Property, Signal, QObject
from PySide2.QtGui import QGuiApplication, QKeySequence

class Controller(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.clock = "00:00"
        self.minutes = 2

    @Property(float)
    def val(self):
        return self.minutes
    
    @Slot()
    def quit(self):
        print('manually killing app')
        QGuiApplication.quit()

    @Slot(str)
    def log(self, msg):
        print(msg)