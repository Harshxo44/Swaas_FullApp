import 'package:flutter/material.dart';

class WaterScreen extends StatelessWidget {
  const WaterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final sources = [
      {
        "name": "River A",
        "level": "High",
        "contamination": "Chemical runoff & bacteria detected.",
        "solution": "Use purification plants. Avoid direct consumption.",
      },
      {
        "name": "Lake B",
        "level": "Medium",
        "contamination": "Moderate algae bloom affecting water clarity.",
        "solution": "Promote controlled fishing, add water treatment.",
      },
      {
        "name": "Village Well",
        "level": "Low",
        "contamination": "Minor bacterial traces found.",
        "solution": "Chlorinate water and monitor regularly.",
      },
    ];

    Color getRiskColor(String level) {
      switch (level) {
        case "High":
          return Colors.redAccent;
        case "Medium":
          return Colors.orangeAccent;
        case "Low":
          return Colors.greenAccent;
        default:
          return Colors.grey;
      }
    }

    Icon getRiskIcon(String level) {
      switch (level) {
        case "High":
          return const Icon(Icons.warning, color: Colors.redAccent);
        case "Medium":
          return const Icon(Icons.error, color: Colors.orangeAccent);
        case "Low":
          return const Icon(Icons.check_circle, color: Colors.greenAccent);
        default:
          return const Icon(Icons.info, color: Colors.white);
      }
    }

    return Scaffold(
      appBar: AppBar(title: const Text("Water Sources")),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: sources.length,
        itemBuilder: (context, index) {
          final source = sources[index];
          final level = source["level"] ?? "Unknown";

          return Card(
            margin: const EdgeInsets.only(bottom: 16),
            elevation: 4,
            color: Colors.grey[900],
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12)),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      getRiskIcon(level),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Text(
                          source["name"] ?? "Unknown Source",
                          style: const TextStyle(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                              color: Colors.tealAccent),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Text(
                    "Risk Level: $level",
                    style: TextStyle(
                        fontSize: 16,
                        color: getRiskColor(level),
                        fontWeight: FontWeight.w600),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    "Issue: ${source["contamination"] ?? ""}",
                    style: const TextStyle(color: Colors.white70),
                  ),
                  const SizedBox(height: 12),
                  Text(
                    "✅ Solution: ${source["solution"] ?? ""}",
                    style: const TextStyle(color: Colors.greenAccent),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
