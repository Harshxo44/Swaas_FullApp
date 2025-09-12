import 'package:flutter/material.dart';

class EducationScreen extends StatelessWidget {
  const EducationScreen({super.key});

  final List<Map<String, String>> educationTopics = const [
    {
      "title": "Waterborne Diseases",
      "description": "Learn about common diseases caused by contaminated water and their prevention.",
      "icon": "💧",
    },
    {
      "title": "Safe Drinking Practices",
      "description": "Tips to ensure water is clean and safe for consumption.",
      "icon": "🧴",
    },
    {
      "title": "Hygiene Awareness",
      "description": "Understanding personal and community hygiene to prevent illness.",
      "icon": "🧼",
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Education")),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: educationTopics.map((topic) {
            return Card(
              margin: const EdgeInsets.only(bottom: 16),
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12)),
              elevation: 4,
              child: ListTile(
                leading: Text(
                  topic["icon"]!,
                  style: const TextStyle(fontSize: 32),
                ),
                title: Text(
                  topic["title"]!,
                  style: const TextStyle(
                      fontWeight: FontWeight.bold, fontSize: 18),
                ),
                subtitle: Padding(
                  padding: const EdgeInsets.only(top: 8),
                  child: Text(
                    topic["description"]!,
                    style: const TextStyle(color: Colors.black87),
                  ),
                ),
              ),
            );
          }).toList(),
        ),
      ),
    );
  }
}
