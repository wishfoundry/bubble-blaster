import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
import QtQuick.Shapes 1.11
import QtQuick.Controls.Material 2.4
import "./" as App

Rectangle {

    id: pageRect
    x: 0
    y: 0
    color: "#4AB4C0"
    anchors {
        left: parent.left
        right: parent.right
        top: parent.top
        bottom: parent.bottom
    }

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
            width: 150
            y: -2
            from: 10
            to: 100
            value: 100

            onValueChanged: {
                app.brightness(value)
            }

            App.MaterialIcon {
                id: brightnessIcon
                anchors.left: brightnessSlider.right
                anchors.verticalCenter: brightnessSlider.verticalCenter
                name: "brightness-2"
                color: "#257E88"

            }
        }

        Slider {
            id: audioSlider
            anchors.right: parent.right
            anchors.rightMargin: 50
            width: 150
            y: -2
            from: 1
            to: 100
            value: 100
            stepSize: 1

            onValueChanged: {
                app.volume(value)
            }

            App.MaterialIcon {
                id: volumeIcon
                anchors.left: audioSlider.right
                anchors.verticalCenter: audioSlider.verticalCenter
                name: "volume-high"
                color: "#257E88"
            }
        }
    }


    App.RunButton {
        id: goBtn
        displayTime: app.displayTime
        y: ((pageRect.height - (logoBar.height  + toolbar.height + 60)) / 2)
        // x: (parent.width / 2) - (138 / 2)
        anchors.horizontalCenter: parent.horizontalCenter
    }

    

    Slider {
        id: timeSlider
        from: app.MIN_TIME
        to: app.MAX_TIME
        stepSize: 1
        snapMode: Slider.SnapAlways
        value: app.minute

        y: parent.height - 50
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.leftMargin: 50
        anchors.rightMargin: 50
        anchors.bottomMargin: 30

        onValueChanged: {
            app.minute = value
        }
        Shape {
            id: tripath
            height: 12
            width: timeSlider.width 
            anchors.right: timeSlider.right
            anchors.rightMargin: 6
            anchors.verticalCenter: timeSlider.verticalCenter
            smooth: true
            antialiasing: true
            layer.enabled: true
            layer.samples: 4
            ShapePath {
                fillColor: '#80CBC4'
                // fillRule: ShapePath.WindingFill
                strokeWidth: 0
                strokeColor: 'transparent'
                startX: 0
                startY: tripath.height / 2
                PathLine { x: tripath.width; y: 0 }
                PathLine { x: tripath.width; y: tripath.height }
            }
        }

        App.MaterialIcon {
            id: rinseIcon
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: -6
            name: "water"
            color: "#257E88"
            size: 20
        }

        
        App.MaterialIcon {
            id: cleanIcon
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: 19
            visible: false
            name: "account-star"
            color: "#257E88"
            size: 20
        }

        App.MaterialIcon {
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: 49
            name: "circle-outline"
            color: "#257E88"
            size: 20
        }

        App.MaterialIcon {
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: 177
            name: "circle-slice-2"
            color: "#257E88"
            size: 20
        }

        App.MaterialIcon {
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: 328
            name: "circle-slice-4"
            color: "#257E88"
            size: 20
        }

        App.MaterialIcon {
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: 505
            name: "circle-slice-6"
            color: "#257E88"
            size: 20
        }

        App.MaterialIcon {
            anchors.top: timeSlider.bottom
            anchors.topMargin: -10
            x: 682
            name: "circle-slice-8"
            color: "#257E88"
            size: 20
        }
    }
}