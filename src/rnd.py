import os
import sys
import signal
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickView
from PySide2.QtGui import QGuiApplication, QKeySequence
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTimer, QUrl
from Controller import Controller

# def interrupt_handler():
#     """Handle KeyboardInterrupt: quit application."""
#     seq = QKeySequence(tr('Ctrl+C'))
#     QGuiApplication.quit()

def filePath(fileName):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))

def onKey(self, event):
    if QKeySequence.Copy == QKeySequence(event.key() + int(event.modifiers())):
        print('close me')
        QGuiApplication.quit()

if __name__ == '__main__':
    # os.environ['QT_QPA_PLATFORM'] = 'eglfs'
    # os.environ['QT_QPA_EGLFS_ALWAYS_SET_MODE'] = '1'
    # os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=true'
    # QT_LOGGING_RULES="qt.qpa.eglfs.kms=true"
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QGuiApplication(sys.argv)
    qml_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "mikki.qml"))

    ctrl = Controller()
    useEngine = True
    if useEngine:
        engine = QQmlApplicationEngine()
        engine.load(filePath("app.qml"))
        engine.rootContext().setContextProperty('app', ctrl)
        # win = engine.rootObjects[0]
        # win.show()
    else:
        view = QQuickView()
        view.setMinimumHeight(480)
        view.setMinimumWidth(800)
        view.setSource(QUrl.fromLocalFile(qml_file))
        view.setResizeMode(QQuickView.SizeRootObjectToView)
        if view.status() == QQuickView.Error:
            sys.exit(-1)
        view.show()

    QTimer.singleShot(9000, lambda : app.quit())

    # enable Ctrl-C to quit

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())
    if useEngine:
        del engine
    else:
        del view
