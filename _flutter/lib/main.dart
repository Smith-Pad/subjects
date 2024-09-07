import 'package:flutter/material.dart';

// Global variables for UI customization
class GlobalStyles {
  static Color backgroundColor = Colors.black;
  static Color textColor = Colors.white;
  static String topHeaderText = "Subjects";
  static TextAlign topHeaderTextAlign = TextAlign.left;

  static void updateBackgroundColor(Color color) {
    backgroundColor = color;
  }

  static void updateTextColor(Color color) {
    textColor = color;
  }

  static void updateTopHeaderText(String text) {
    topHeaderText = text;
  }

  static void updateTopHeaderTextAlign(TextAlign textAlign) {
    topHeaderTextAlign = textAlign;
  }
}

// Main app widget
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        scaffoldBackgroundColor: GlobalStyles.backgroundColor,
        textTheme: TextTheme(
          bodyMedium: TextStyle(color: GlobalStyles.textColor), // Use bodyText2 for modern Flutter versions
        ),
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            GlobalStyles.topHeaderText,
            textAlign: GlobalStyles.topHeaderTextAlign,
          ),
        ),
        body: Center(
          child: Text('Hello World', style: TextStyle(color: GlobalStyles.textColor)),
        ),
      ),
    );
  }
}

void main() {
  runApp(MyApp());
}
