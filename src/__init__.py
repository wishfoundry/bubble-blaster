
import sys
import os
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QLabel
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, Slot

@Slot()
def say_hello():
    print("Button clicked, Hello!")


if __name__ == "__main__":
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QApplication(sys.argv)
    # button = QPushButton("Click me")
    # button.clicked.connect(say_hello)
    # button.show()
    view = QQuickView()
    
    view.setSource(QUrl.fromLocalFile("./src/mikki.qml"))
    view.setMinimumHeight(400)
    view.setMinimumWidth(600)
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()
    # label = QLabel("Hello World")
    # label.show()
    sys.exit(app.exec_())
