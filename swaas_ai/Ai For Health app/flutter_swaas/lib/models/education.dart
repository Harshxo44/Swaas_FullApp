class Education {
  String title;
  String content;
  String category;

  Education({
    required this.title,
    required this.content,
    required this.category,
  });

  factory Education.fromJson(Map<String, dynamic> json) => Education(
        title: json['title'],
        content: json['content'],
        category: json['category'],
      );

  Map<String, dynamic> toJson() => {
        'title': title,
        'content': content,
        'category': category,
      };
}
