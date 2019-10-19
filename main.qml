import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.5
import QtQuick.Controls.Material 2.3
import QtGraphicalEffects 1.12
import QtQuick.Extras 1.4
import QtQuick.Layouts 1.3

// Item {
//     Material.theme: Material.Dark
//     Material.accent: Material.Purple
//     x:0
//     y:0
//     width: navigation.width
//     height: navigation.height

Rectangle {
    
    // Material.theme: Material.Dark
    // Material.accent: Material.Green

    id: pageRect
    x: 0
    y: 0
    // width: parent.width
    // height: parent.height

    color: "#303030"
    LinearGradient {
        id: blueGradient
        cached: true
        anchors.fill: parent
        start: Qt.point(parent.width, 0)
        end: Qt.point(0, parent.height)

        gradient: Gradient {
            GradientStop {
                position: 1
                color: "#2196f3"
            }

            GradientStop {
                position: 0
                color: "#21cbf3"
            }
        }
    }

    

    RowLayout {
        id: mainGroup
        anchors.centerIn: pageRect

        ColumnLayout {
                // x: -100
                // y: 154
                // width: 200
                // height: 100
                // anchors.centerIn: pageRect

                RoundButton {
                    id: goBtn
                    text: timeSlider.value.toString() + " Min"
                    anchors.horizontalCenter: mainGroup.horizontalCenter
                    flat: false
                    height: 100
                    radius: 11

                    LinearGradient {
                        source: goBtn
                        anchors.fill: parent
                        start: Qt.point(parent.width, 0)
                        end: Qt.point(0, parent.height)
                        gradient: Gradient {
                            GradientStop {
                                position: 0
                                color: "#fe6b8b"
                            }

                            GradientStop {
                                position: 1
                                color: "#ff8e53"
                            }
                        }
                    }
                }

                

                Slider {
                    id: timeSlider
                    from: 3
                    to: 21
                    stepSize: 3
                }
            }

            Slider {
                id: audioSlider
                from: 0
                to: 10
                stepSize: 2.5
                orientation: Qt.Vertical
            }
    }
    
}
// }


/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
