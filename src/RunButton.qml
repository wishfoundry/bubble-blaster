import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
import "./" as App


Rectangle {

    property alias displayTime: timeText.text

    id: goBtn
    
    width: 138
    height: 138
    radius: width / 2
    color: app.isRunning ? "#257E88" : "#93F4FF"
    MouseArea {
        anchors.fill: parent
        onClicked: {
            // parent.color = "#FD7503"
            // goBtn.color = "#257E88"
            // btnIcon.name = "pause"
            // btnIcon.color = "white"
            app.toggle()
        }

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

    App.MaterialIcon {
        id: btnIcon
        name: app.isRunning ? "stop" : "play"
        size: 100
        color: app.isRunning ? "white" : "#257E88"
        anchors.centerIn: parent
    }

    Text {
        id: timeText
        anchors.top: goBtn.bottom
        color: "#257E88"
        font.pixelSize: 30
        anchors.horizontalCenter: goBtn.horizontalCenter 
    }
}
