import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.5
import QtQuick.Controls.Material 2.3
import QtQuick.Layouts 1.3

Rectangle {

    id: pageRect
    x: 0
    y: 0
    color: "#4AB4C0"

    Material.theme: Material.Dark
    Material.accent: Material.Teal
    Material.primary: Material.BlueGrey

    Rectangle {

        id: logoBar
        x: 0
        y: 0
        width: parent.width
        height: 40
        color: "#ffffff"

        Image {
            id: logo
            source: "logo.jpg"
            width: 140
            height: width / 4
            y: 0
            x: (parent.width / 2) - (width / 2)
        }
    }

    Rectangle {

        id: toolbar
        x: 0
        y: 40
        width: parent.width
        height: 40
        color: "#3Da4Af"

        Slider {
            id: brightnessSlider
            anchors.left: parent.left
            anchors.leftMargin: 50
            width: 100
            y: -2
        }

        Slider {
            id: audioSlider
            anchors.right: parent.right
            anchors.rightMargin: 50
            width: 100
            y: -2
        }
    }

    Rectangle {
        id: goBtn
        y: 150
        x: (parent.width / 2) - (138 / 2)
        width: 138
        height: 138
        radius: width / 2
        color: "#93F4FF"
        MouseArea {
            anchors.fill: parent
            onClicked: { parent.color = "#FD7503" }

            Item {
                function countdown(startTime) {
                    var start = new Date(startTime);
                    var now = new Date();
                    var timeDiff = start.getTime() - now.getTime();
                    if (timeDiff <= 0) {
                        clearTimeout(timer);
                    }
                    var seconds = Math.floor(timeDiff / 1000);
                    var minutes = Math.floor(seconds / 60);
                    var hours = Math.floor(minutes / 60);
                    var days = Math.floor(hours / 24);

                    hours %= 24;
                    minutes %= 60;
                    seconds %= 60;

                    var output = days + " days" + "," + hours + " hours, " + minutes + " minutes, " + seconds + " seconds."
                    return output;
                    var timer = setTimeout('cdtd()', 1000)
                }
            }
        }

        Text {
            anchors.top: goBtn.bottom
            color: "#ffffff"
            text: "00:00"
            font.pixelSize: 24
            anchors.horizontalCenter: goBtn.horizontalCenter 
        }
    }

    


    Slider {
        id: timeSlider
        from: 2
        to: 30
        stepSize: 1
        snapMode: Slider.SnapAlways
        
        y: parent.height - 50
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.leftMargin: 50
        anchors.rightMargin: 50
        anchors.bottomMargin: 30
    }
}