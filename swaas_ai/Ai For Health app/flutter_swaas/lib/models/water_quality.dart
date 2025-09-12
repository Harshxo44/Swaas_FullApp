class WaterQuality {
  String location;
  String district;
  String waterSourceType;
  double phLevel;
  double turbidity;
  int bacterialCount;
  String contaminationLevel;
  String testedBy;

  WaterQuality({
    required this.location,
    required this.district,
    required this.waterSourceType,
    required this.phLevel,
    required this.turbidity,
    required this.bacterialCount,
    required this.contaminationLevel,
    required this.testedBy,
  });

  factory WaterQuality.fromJson(Map<String, dynamic> json) => WaterQuality(
        location: json['location'],
        district: json['district'],
        waterSourceType: json['waterSourceType'],
        phLevel: json['phLevel'],
        turbidity: json['turbidity'],
        bacterialCount: json['bacterialCount'],
        contaminationLevel: json['contaminationLevel'],
        testedBy: json['testedBy'],
      );

  Map<String, dynamic> toJson() => {
        'location': location,
        'district': district,
        'waterSourceType': waterSourceType,
        'phLevel': phLevel,
        'turbidity': turbidity,
        'bacterialCount': bacterialCount,
        'contaminationLevel': contaminationLevel,
        'testedBy': testedBy,
      };
}
