import '../models/health_report.dart';
import '../models/water_quality.dart';

String evaluateOutbreakRisk(List<HealthReport> reports, List<WaterQuality> waterData, String village) {
  int symptomCount = reports
      .where((r) => r.location == village)
      .fold(0, (sum, r) => sum + r.symptoms.length);

  bool highContamination = waterData
      .any((w) => w.location == village && (w.contaminationLevel == 'High' || w.contaminationLevel == 'Critical'));

  if (symptomCount > 5 || highContamination) return "High";
  if (symptomCount >= 3) return "Moderate";
  return "Low";
}
