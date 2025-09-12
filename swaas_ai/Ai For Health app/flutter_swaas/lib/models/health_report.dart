class HealthReport {
  String patientName;
  int age;
  String gender;
  String location;
  String district;
  List<String> symptoms;
  String severity;
  String waterSource;
  String reportedBy;
  String contactNumber;
  String notes;
  String status;

  HealthReport({
    required this.patientName,
    required this.age,
    required this.gender,
    required this.location,
    required this.district,
    required this.symptoms,
    required this.severity,
    required this.waterSource,
    required this.reportedBy,
    required this.contactNumber,
    required this.notes,
    required this.status,
  });

  factory HealthReport.fromJson(Map<String, dynamic> json) => HealthReport(
        patientName: json['patientName'],
        age: json['age'],
        gender: json['gender'],
        location: json['location'],
        district: json['district'],
        symptoms: List<String>.from(json['symptoms']),
        severity: json['severity'],
        waterSource: json['waterSource'],
        reportedBy: json['reportedBy'],
        contactNumber: json['contactNumber'],
        notes: json['notes'],
        status: json['status'],
      );

  Map<String, dynamic> toJson() => {
        'patientName': patientName,
        'age': age,
        'gender': gender,
        'location': location,
        'district': district,
        'symptoms': symptoms,
        'severity': severity,
        'waterSource': waterSource,
        'reportedBy': reportedBy,
        'contactNumber': contactNumber,
        'notes': notes,
        'status': status,
      };
}
