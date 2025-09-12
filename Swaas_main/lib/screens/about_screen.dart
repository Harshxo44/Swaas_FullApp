import 'package:flutter/material.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("About")),
      body: const Padding(
        padding: EdgeInsets.all(16),
        child: Text(
          "Swaas Health App\n\nVersion: 1.0.0\n\nThis app helps monitor "
          "waterborne diseases, provides alerts, educational resources, "
          "and tracks reports for safer communities.",
        ),
      ),
    );
  }
}
