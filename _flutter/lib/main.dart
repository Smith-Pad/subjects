import 'package:flutter/material.dart';

// Global variables for UI customization
class GlobalStyles {
  static Color backgroundColor = Colors.black;
  static Color textColor = Colors.white;
  static String topHeaderText = "Subjects";
  static TextAlign topHeaderTextAlign = TextAlign.left;

  // Update the global UI background color
  static void setBackgroundColor(Color color) {
    backgroundColor = color;
  }

  // Update the global text color
  static void setTextColor(Color color) {
    textColor = color;
  }

  // Update the top header text
  static void setTopHeaderText(String text) {
    topHeaderText = text;
  }

  // Update the alignment of the top header text
  static void setTopHeaderTextAlign(TextAlign textAlign) {
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
          bodyLarge: TextStyle(color: GlobalStyles.textColor),
        ),
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            GlobalStyles.topHeaderText,
            textAlign: GlobalStyles.topHeaderTextAlign,
          ),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Align(
            alignment: Alignment.centerLeft, // Align the content to the left
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start, // Align children to the left
              children: <Widget>[
                Text(
                  'Middle Section',
                  style: TextStyle(color: GlobalStyles.textColor),
                ),
                const SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {
                    // Button action
                  },
                  child: const Text('This is a button'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

void main() {
  // You can update global styles before running the app
  GlobalStyles.setBackgroundColor(Colors.black);
  GlobalStyles.setTextColor(Colors.white);
  GlobalStyles.setTopHeaderText("Subjects");
  GlobalStyles.setTopHeaderTextAlign(TextAlign.left);

  runApp(MyApp());
}
