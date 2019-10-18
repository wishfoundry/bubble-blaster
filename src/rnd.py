import os
import sys
import PySide2.QtQml
from PySide2.QtQuick import QQuickView
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTimer, QUrl

if __name__ == '__main__':
    # os.environ['QT_QPA_PLATFORM'] = 'eglfs'
    # os.environ['QT_QPA_EGLFS_ALWAYS_SET_MODE'] = '1'
    # os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=true'
    # QT_LOGGING_RULES="qt.qpa.eglfs.kms=true"
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QApplication(sys.argv)
    qml_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "mikki.qml"))
    view = QQuickView()
    view.setMinimumHeight(480)
    view.setMinimumWidth(800)
    view.setSource(QUrl.fromLocalFile(qml_file))
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()
    QTimer.singleShot(9000, lambda : app.quit())
    app.exec_()
    del view
