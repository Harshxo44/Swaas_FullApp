class Alert {
  String title;
  String description;
  String alertType;
  String severity;
  String location;
  String district;
  String issuedBy;

  Alert({
    required this.title,
    required this.description,
    required this.alertType,
    required this.severity,
    required this.location,
    required this.district,
    required this.issuedBy,
  });

  factory Alert.fromJson(Map<String, dynamic> json) => Alert(
        title: json['title'],
        description: json['description'],
        alertType: json['alertType'],
        severity: json['severity'],
        location: json['location'],
        district: json['district'],
        issuedBy: json['issuedBy'],
      );

  Map<String, dynamic> toJson() => {
        'title': title,
        'description': description,
        'alertType': alertType,
        'severity': severity,
        'location': location,
        'district': district,
        'issuedBy': issuedBy,
      };
}
