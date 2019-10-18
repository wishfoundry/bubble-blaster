import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4
import QtQuick.Layouts 1.3

Rectangle {

    id: pageRect
    x: 0
    y: 0
    color: "#4AB4C0"

    // Layout.fillWidth: true
    anchors.fill: parent
    height: 50

    MouseArea {
            anchors.fill: parent
            onClicked: { 
                parent.color = "#FD7503" 
            }
    }
}