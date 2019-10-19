import os
import sys
import signal
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickView
from PySide2.QtGui import QGuiApplication, QKeySequence, QFontDatabase
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTimer, QUrl
from Controller import Controller

def filePath(fileName):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))

def minutes(i):
    return i * 60 * 1000

if __name__ == '__main__':
    # os.environ['QT_QPA_PLATFORM'] = 'eglfs'
    # os.environ['QT_QPA_EGLFS_ALWAYS_SET_MODE'] = '1'
    # os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=true'
    # QT_LOGGING_RULES="qt.qpa.eglfs.kms=true"
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QGuiApplication(sys.argv)
    QFontDatabase.addApplicationFont(filePath("resources/materialdesignicons-webfont.ttf"))

    ctrl = Controller()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('app', ctrl)
    engine.load(QUrl.fromLocalFile(filePath("app.qml")))

    # safety timeout, must go away!
    # QTimer.singleShot(minutes(10), lambda : app.quit())

    # enable Ctrl-C to quit from cli
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
