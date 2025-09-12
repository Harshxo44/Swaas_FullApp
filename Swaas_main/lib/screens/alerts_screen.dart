import 'package:flutter/material.dart';

class AlertsScreen extends StatelessWidget {
  const AlertsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final alerts = [
      {
        "title": "River A Contamination",
        "level": "High",
        "description": "Heavy chemical contamination detected.",
      },
      {
        "title": "Village B Water Alert",
        "level": "Medium",
        "description": "Bacterial presence higher than normal.",
      },
      {
        "title": "Well C Alert",
        "level": "Low",
        "description": "Minor impurities detected.",
      },
    ];

    return Scaffold(
      appBar: AppBar(title: const Text("Active Alerts")),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: alerts.length,
        itemBuilder: (context, index) {
          final alert = alerts[index];
          Color riskColor;
          if (alert["level"] == "High") {
            riskColor = Colors.redAccent;
          } else if (alert["level"] == "Medium") {
            riskColor = Colors.orangeAccent;
          } else {
            riskColor = Colors.greenAccent;
          }

          return Card(
            margin: const EdgeInsets.only(bottom: 16),
            color: Colors.grey[900],
            shape:
                RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    alert["title"]!,
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.tealAccent,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    "Risk Level: ${alert["level"]}",
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                      color: riskColor,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    alert["description"]!,
                    style: const TextStyle(color: Colors.white70),
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
