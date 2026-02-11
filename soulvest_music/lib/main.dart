import 'package:flutter/material.dart';
import 'chant_screen.dart';

void main() {
  runApp(SoulvestApp());
}

class SoulvestApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Soulvest Music',
      theme: ThemeData(
        scaffoldBackgroundColor: Color(0xFF1E1E2F),
        appBarTheme: AppBarTheme(backgroundColor: Color(0xFF2C2C54)),
        textTheme: TextTheme(
          bodyLarge: TextStyle(color: Colors.white, fontSize: 20),
          bodyMedium: TextStyle(color: Colors.white70),
        ),
      ),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  final String affirmation = "I am healing. I am whole. I am becoming the sanctuary I seek.";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Soulvest Music')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("🌌 Welcome to Soulvest", style: Theme.of(context).textTheme.bodyLarge),
            SizedBox(height: 20),
            Text("🧘 Affirmation:", style: Theme.of(context).textTheme.bodyMedium),
            SizedBox(height: 10),
            Container(
              padding: EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Color(0xFF2C2C54),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Text(affirmation, style: TextStyle(color: Colors.white)),
            ),
            SizedBox(height: 30),
            ElevatedButton.icon(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ChantScreen()),
                );
              },
              icon: Icon(Icons.music_note),
              label: Text("Explore Chants"),
              style: ElevatedButton.styleFrom(backgroundColor: Color(0xFF6A5ACD)),
            ),
          ],
        ),
      ),
    );
  }
}
