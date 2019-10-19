import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
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
            width: 100
            y: -2
            from: 1
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
            width: 100
            y: -2
            from: 1
            to: 100
            value: 100

            // onValueChanged: {
            //     app.brightness(value)
            // }

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
        from: 1
        to: 30
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
    }
}