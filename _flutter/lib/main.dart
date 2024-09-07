import 'package:flutter/material.dart';

// Define a class to manage global styles
class GlobalStyles {
  static Color backgroundColor = Colors.black;
  static Color textColor = Colors.white;
  static String textContent = 'Hello World';
  static double textSize = 40.0;

  // Function to update UI colors
  static void updateUiColors() {
    backgroundColor = Colors.black;
    textColor = Colors.white;
  }

  // Function to update header colors
  static void updateHeaderColors() {
    backgroundColor = Colors.black;
    textColor = Colors.white;
  }

  // Function to update header content
  static void updateHeaderContent() {
    textContent = 'Subjects';
    textSize = 40.0;
  }
}

void main() {
  // Apply the initial setup
  GlobalStyles.updateUiColors();
  GlobalStyles.updateHeaderColors();
  GlobalStyles.updateHeaderContent();

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          GlobalStyles.textContent,
          style: TextStyle(color: GlobalStyles.textColor),
        ),
        backgroundColor: GlobalStyles.backgroundColor,
      ),
      backgroundColor: GlobalStyles.backgroundColor,
      body: Center(
        child: Text(
          GlobalStyles.textContent,
          style: TextStyle(color: GlobalStyles.textColor, fontSize: GlobalStyles.textSize),
        ),
      ),
    );
  }
}
