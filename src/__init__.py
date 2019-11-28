import os
import sys
import signal
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickView
from PySide2.QtGui import QGuiApplication, QKeySequence, QFontDatabase
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTimer, QUrl, QFileSystemWatcher
from Controller import Controller
from gpio import cleanup

def filePath(fileName):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))

def appQmlFile():
    return QUrl.fromLocalFile(filePath("app.qml"))

def minutes(i):
    return i * 60 * 1000

isRasperry = os.uname()[4].startswith('arm')

if __name__ == '__main__':
    if isRasperry:
        os.environ['QT_QPA_PLATFORM'] = 'eglfs'
        os.environ['QT_QPA_EGLFS_HIDECURSOR'] = '1'
        os.environ['QT_QPA_EGLFS_ALWAYS_SET_MODE'] = '1'
        # os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=true'
        # QT_LOGGING_RULES="qt.qpa.eglfs.kms=true"
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QGuiApplication(sys.argv)
    QFontDatabase.addApplicationFont(filePath("resources/materialdesignicons-webfont.ttf"))

    ctrl = Controller()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('app', ctrl)
    engine.load(appQmlFile())

    # safety timeout, must go away!
    # QTimer.singleShot(minutes(10), lambda : app.quit())

    # enable Ctrl-C to quit from cli
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # timer = QTimer()
    # timer.start(500)  # You may change this if you wish.
    # timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.
    # if not isRasperry:
    #     def reload():
    #         print('files changed!')
    #         win = engine.rootObjects()[0]
    #         win.close()
    #         # win.setSource(QUrl())
    #         engine.clearComponentCache()
    #         engine.load(appQmlFile())
    #         QTimer.singleShot(200, lambda : engine.rootObjects()[0].show())
    #         # win.setSource(appQmlFile())
    #         # engine.rootObjects()[0].show()
    #     watcher = QFileSystemWatcher(app)
    #     watcher.addPath(os.path.abspath(os.path.dirname(__file__)))
    #     watcher.directoryChanged.connect(reload)

    app.aboutToQuit.connect(lambda : cleanup())

    sys.exit(app.exec_())
