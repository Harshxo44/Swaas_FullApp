import 'package:flutter/material.dart';

class ReportsScreen extends StatelessWidget {
  const ReportsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final reports = [
      {
        "title": "River A Contamination",
        "level": "High",
        "description": "Detected harmful bacteria and high chemical runoff.",
        "solution": "Boil water before use. Install purification units.",
      },
      {
        "title": "Groundwater Nitrates",
        "level": "Medium",
        "description": "Nitrate levels above safe limit in groundwater samples.",
        "solution": "Avoid direct drinking. Use nitrate-removal filters.",
      },
      {
        "title": "Village Well Bacteria",
        "level": "Low",
        "description": "Minor bacterial contamination found in well.",
        "solution": "Chlorinate well. Promote hygiene awareness.",
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
          return Colors.white;
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
      appBar: AppBar(title: const Text("Reports")),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: reports.length,
        itemBuilder: (context, index) {
          final report = reports[index];
          final level = report["level"] ?? "Unknown";

          return Card(
            margin: const EdgeInsets.only(bottom: 16),
            color: Colors.grey[900],
            elevation: 4,
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
                          report["title"] ?? "No title",
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
                    report["description"] ?? "",
                    style: const TextStyle(color: Colors.white70),
                  ),
                  const SizedBox(height: 12),
                  Text(
                    "✅ Solution: ${report["solution"] ?? ""}",
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
