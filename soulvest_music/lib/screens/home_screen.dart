import 'package:flutter/material.dart';
import 'rituals_screen.dart';
import 'healing_screen.dart';

class HomeScreen extends StatelessWidget {
  final String affirmation = "I am healing. I am whole. I am becoming the sanctuary I seek.";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Soulvest Music")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(affirmation, style: TextStyle(fontSize: 18)),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text("My Rituals"),
              onPressed: () => Navigator.push(context,
                MaterialPageRoute(builder: (_) => RitualsScreen())),
            ),
            ElevatedButton(
              child: Text("Healing Practices"),
              onPressed: () => Navigator.push(context,
                MaterialPageRoute(builder: (_) => HealingScreen())),
            ),
          ],
        ),
      ),
    );
  }
}
