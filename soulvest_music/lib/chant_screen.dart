import 'package:flutter/material.dart';

class ChantScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("🕉️ Om Namah Shivaya")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text("Radhe Krishna\n(Love. Heart Expansion.)", style: Theme.of(context).textTheme.bodyLarge),
            SizedBox(height: 20),
            Container(
              padding: EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Color(0xFF2C2C54),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Text("Chant playback will appear here.", style: TextStyle(color: Colors.white70)),
            ),
          ],
        ),
      ),
    );
  }
}
