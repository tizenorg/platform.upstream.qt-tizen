import QtQuick 2.0
import QtMultimedia 5.0

Rectangle {
    width: 480
    height: 270

    MediaPlayer {
        id: player
        source: "/usr/share/media/videos/AmazingNature_480p.mp4" // Point this to a suitable video file
        autoPlay: true
    }

    VideoOutput {
        source: player
        anchors.fill: parent
    }
}
