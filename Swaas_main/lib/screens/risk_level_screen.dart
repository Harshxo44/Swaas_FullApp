import 'package:flutter/material.dart';

class RiskLevelScreen extends StatelessWidget {
  const RiskLevelScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final riskData = [
      {
        "location": "River A",
        "risk": "High",
        "description": "Detected heavy chemical contamination.",
      },
      {
        "location": "Village B",
        "risk": "Medium",
        "description": "Bacterial presence higher than normal.",
      },
      {
        "location": "Well C",
        "risk": "Low",
        "description": "Safe for drinking, minor impurities detected.",
      },
    ];

    Color getRiskColor(String risk) {
      switch (risk) {
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

    return Scaffold(
      appBar: AppBar(title: const Text("Risk Levels")),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: riskData.length,
        itemBuilder: (context, index) {
          final risk = riskData[index];
          final riskLevel = risk["risk"] ?? "Unknown";

          return Card(
            margin: const EdgeInsets.only(bottom: 16),
            elevation: 4,
            shape:
                RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    risk["location"] ?? "Unknown Location",
                    style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        color: Colors.white),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    risk["description"] ?? "",
                    style: const TextStyle(color: Colors.white70),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    "Risk: $riskLevel",
                    style: TextStyle(
                        fontWeight: FontWeight.bold, color: getRiskColor(riskLevel)),
                  ),
                ],
              ),
            ),
            color: Colors.grey[900],
          );
        },
      ),
    );
  }
}
