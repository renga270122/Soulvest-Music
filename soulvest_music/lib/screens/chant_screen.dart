import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';

class ChantScreen extends StatefulWidget {
  @override
  _ChantScreenState createState() => _ChantScreenState();
}

class _ChantScreenState extends State<ChantScreen> {
  final AudioPlayer player = AudioPlayer();
  bool isPlaying = false;

  void togglePlayback() async {
    if (isPlaying) {
      await player.pause();
    } else {
      await player.play(AssetSource('chants/om_namah_shivaya.mp3'));
    }
    setState(() {
      isPlaying = !isPlaying;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("OM Namah Shivaya")),
      body: Center(
        child: ElevatedButton.icon(
          icon: Icon(isPlaying ? Icons.pause : Icons.play_arrow),
          label: Text(isPlaying ? "Pause" : "Play"),
          onPressed: togglePlayback,
        ),
      ),
    );
  }
}
