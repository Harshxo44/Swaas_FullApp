// lib/data/mock_reports.dart
import '../models/health_report.dart';

// Mock list of health reports
List<HealthReport> mockReports = [
  HealthReport(
    patientName: "Ramesh Kumar",
    age: 25,
    gender: "Male",
    location: "Village A",
    district: "District 1",
    symptoms: ["Diarrhea", "Fever"],
    severity: "Moderate",
    waterSource: "Well 1",
    reportedBy: "Health Worker 1",
    contactNumber: "9876543210",
    notes: "N/A",
    status: "Open",
  ),
  HealthReport(
    patientName: "Sita Devi",
    age: 30,
    gender: "Female",
    location: "Village B",
    district: "District 1",
    symptoms: ["Vomiting"],
    severity: "High",
    waterSource: "River 2",
    reportedBy: "Health Worker 2",
    contactNumber: "9876543211",
    notes: "Observed dehydration",
    status: "Closed",
  ),
  HealthReport(
    patientName: "Raju Patel",
    age: 12,
    gender: "Male",
    location: "Village A",
    district: "District 1",
    symptoms: ["Diarrhea"],
    severity: "Low",
    waterSource: "Well 1",
    reportedBy: "Health Worker 1",
    contactNumber: "9876543212",
    notes: "",
    status: "Open",
  ),
];
