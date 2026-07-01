**Personal Expense Tracker (Python CLI Application):**
 **Overview**:

The Personal Expense Tracker is a command-line based Python application designed to help users record, manage, and analyze their daily expenses in a simple and structured way.

The program allows users to continuously enter expenses, categorize them, and then generates a complete summary including statistics and history. It also provides an option to save the report into a text file for future reference.

This project is ideal for beginners who want to strengthen their understanding of Python fundamentals and real-world application development.

 **Project Purpose**:

The main goal of this project is to simulate a real-world expense management system using Python. It helps users:

Track daily spending habits
Organize expenses into categories
Analyze total spending behavior
Generate readable financial summaries
Save reports for offline use

 **Key Features**:
➤ 1. Interactive Expense Input
Users can enter multiple expense amounts one by one.
The program continues running until the user types "done".
Ensures only valid numeric inputs are accepted.
➤ 2. Category Support
Each expense can be assigned a category (e.g., Food, Travel, Bills).
If no category is entered, it defaults to "General".
Categories are automatically formatted (capitalized).
➤ 3. Timestamp Tracking
Every expense is recorded with the exact time of entry.
Helps users track when each expense was added.
➤ 4. Expense History Display
Shows all recorded expenses in a structured table format.

**Displays:**
Serial number
Amount
Category
Time
➤ 5. Category-wise Summary
Automatically groups expenses by category.
Calculates total spending per category.
Helps users understand where most money is spent.
➤ 6. Statistical Analysis

The program calculates key financial insights:

Total Expenses → Sum of all recorded amounts
Average Expense → Mean value of all entries
Highest Expense → Largest single expense with category
Lowest Expense → Smallest expense with category
➤ 7. File Saving Feature
Generates a text report (expenses_report.txt)
Includes:
All expense entries
Timestamp
Total spent
Useful for record keeping or sharing reports
➤ 8. Input Validation & Error Handling
Prevents invalid inputs (letters, negative numbers, zero values)
Uses try-except to handle runtime errors safely
Ensures smooth user experience without crashes

** Concepts Used in This Project**:

This project demonstrates several core Python concepts:

Functions & modular programming
Loops (while, for)
Conditionals (if-else)
Lists & dictionaries
Exception handling (try-except)
File handling (open, write mode)
Date & time module (datetime)
String formatting and alignment

** Project Structure (Logical Flow)**:

Program starts (run_tracker())
User enters expenses repeatedly
Each expense is stored in a list of dictionaries
Total is updated dynamically
After exit:
History is displayed
Category summary is shown
Statistics are calculated
User is asked to save report
File is generated if confirmed

Then the program shows:

Expense History
Category Breakdown
Statistics Summary
Save report option
Sample Report File Output
Expense Tracker Report
==============================

** Learning Outcome**:

By building this project, you learn how to:

Build a complete CLI application in Python
Manage structured data efficiently
Apply real-world logic (expense tracking system)
Handle user input safely
Generate reports programmatically

**Future Improvements (Optional Ideas)**:

Add GUI using Tkinter or PyQt
Store data in a database (SQLite)
Add monthly budgeting system
Export report to Excel or CSV
Add login system for multiple users

**Conclusion**:

This project is a strong beginner-to-intermediate level Python application that demonstrates practical programming skills, real-world logic building, and clean code structuring.

**Developer:**
Laiba Maqbool
