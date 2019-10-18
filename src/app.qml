import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
import QtQuick.Controls.Material 2.4
import "./" as My


ApplicationWindow {
    id: window
    title: qsTr("Test")
    visible: true
    width: 800
    height: 480

    Material.theme: Material.Dark
    Material.accent: Material.Teal
    Material.primary: Material.BlueGrey

    My.Page {
        id: page
        width: window.width
        height: window.height
    }

    // provide a backdoor to close the app
    Shortcut {
        sequences: [StandardKey.Cancel, "Ctrl+C", StandardKey.Backspace, StandardKey.Close]
        context: Qt.ApplicationShortcut
        onActivated: {
            app.quit()
            // Qt.quit()
        }
    }

}