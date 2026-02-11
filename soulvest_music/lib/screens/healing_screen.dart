import 'package:flutter/material.dart';
import 'chant_screen.dart';
import 'meditation_screen.dart';

class HealingScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Healing Practices")),
      body: ListView(
        children: [
          ListTile(
            title: Text("🧘 OM Chanting"),
            onTap: () => Navigator.push(context,
              MaterialPageRoute(builder: (_) => ChantScreen())),
          ),
          ListTile(
            title: Text("🌬️ Kriya Yoga"),
            onTap: () => Navigator.push(context,
              MaterialPageRoute(builder: (_) => MeditationScreen())),
          ),
        ],
      ),
    );
  }
}
