# CSA08 – Python Programming Assignment 4

## Robust Data Processing with Files, Exceptions, Modules and Packages

### Student Details

- **Name:** Sri Vyshnavi
- **Register Number:** [192412488]
- **Course Code:** CSA0811
- **Course Name:** Python Programming
- **Course Outcome:** CO4
- **Assignment:** Assignment 4
- **Total Marks:** 50
- **Python Version:** [Enter Your Python Version]

---

## 1. Introduction

This assignment focuses on robust data processing using Python. It demonstrates file handling, exception handling, custom exceptions, modules and packages.

The programs are designed to process data, identify errors, handle missing files and generate reports. They also demonstrate how Python programs can be organised and maintained effectively.

## 2. Objectives

- To understand Python file handling operations.
- To read and process data from files.
- To identify and handle different types of exceptions.
- To create and use custom exceptions.
- To understand Python modules and packages.
- To develop reliable data-processing applications.
- To analyse program efficiency using Big-O notation.

## 3. Technologies Used

- **Programming Language:** Python
- **Compiler:** Online Python Compiler
- **Libraries Used:** Python Standard Library
- **Modules:** io

No external Python packages are required.

## 4. Repository Structure

```text
CSA08-RegisterNumber-Assignment4/
│
├── Task01/
│   └── Task01_Mess_Bill.py
│
├── Task02/
│   └── Task02_Attendance.py
│
├── Task03/
│   └── Task03_Exception_Handling.py
│
├── Task04/
│   └── Task04_File_Forensics.py
│
├── Task05/
│   └── Task05_Modules.py
│
├── Task06/
│   └── Task06_College_Fest.py
│
├── requirements.txt
└── README.md
```

## 5. Task Descriptions and Results

### Task 1 – File-Processing Design Review: Diagnose and Repair a Poor Script

**Objective:** To identify the problems in a poorly designed file-processing program and develop a safer solution.

**Concepts Used:**
- File handling
- Line-by-line processing
- Functions
- Exception handling
- Rejected record management

**Program:** `Task01_Mess_Bill.py`

**Result:** The program processes mess bill records, calculates the total bill amount and identifies invalid records.

### Task 2 – From Requirement to File-Processing Design: Biometric Attendance Files

**Objective:** To process biometric attendance records and calculate the attendance percentage of students.

**Concepts Used:**
- File processing
- Dictionaries
- Attendance calculation
- Exception handling
- Error logging

**Program:** `Task02_Attendance.py`

**Result:** The program calculates student attendance percentages, identifies students below 75% attendance and displays damaged records.

### Task 3 – Design the Error Handling: Exceptions in the Attendance Processor

**Objective:** To implement exception handling using built-in and custom exceptions.

**Concepts Used:**
- Custom exceptions
- try and except
- else and finally
- raise statement
- raise from statement
- Invalid record validation

**Program:** `Task03_Exception_Handling.py`

**Result:** The program validates attendance records, counts present and absent students, identifies invalid records and handles missing-file errors.

### Task 4 – File and Exception Forensics

**Objective:** To identify and correct errors in a file-handling program.

**Concepts Used:**
- File opening modes
- Append mode
- Newline characters
- with statement
- Error logging
- FileNotFoundError

**Program:** `Task04_File_Forensics.py`

**Result:** The program processes book return records for multiple days and maintains a combined return log and error log.

### Task 5 – The Same Utility Organised Four Ways

**Objective:** To understand different ways of organising Python programs using scripts, modules and packages.

**Concepts Used:**
- Python functions
- Modules
- Packages
- Import statements
- `if __name__ == "__main__"`
- Code reusability

**Program:** `Task05_Modules.py`

**Result:** The program demonstrates attendance calculation, report generation and identification of students absent for three consecutive days in a single-script implementation.

The complete assignment also requires separate demonstrations of:
1. One script
2. One imported module
3. Three modules in one folder
4. A package containing sub-modules

### Task 6 – Design Challenge: College Fest Registration Desk

**Objective:** To develop a registration processing system that validates student information and generates event-wise reports.

**Concepts Used:**
- File processing
- Dictionaries
- Duplicate detection
- String validation
- Exception handling
- Error logging
- Report generation

**Program:** `Task06_College_Fest.py`

**Result:** The program validates registration details, identifies duplicate registrations, checks e-mail addresses, groups participants by events and generates a summary and error log.

## 6. How to Execute the Programs

1. Open a Python compiler.
2. Select Python 3.
3. Open the required task program.
4. Copy and paste the source code.
5. Click the Run button.
6. Check the output.
7. Save the source code and output evidence in the corresponding task folder.

### Execution Commands

```bash
python Task01_Mess_Bill.py
python Task02_Attendance.py
python Task03_Exception_Handling.py
python Task04_File_Forensics.py
python Task05_Modules.py
python Task06_College_Fest.py
```

Run each command from the corresponding task folder, or adjust the path according to your repository structure.

## 7. Complexity Analysis

| Task | Main Operation | Time Complexity |
|---|---|---|
| Task 1 | Processing mess bill records | O(n) |
| Task 2 | Processing attendance records | O(n) |
| Task 3 | Validating attendance records | O(n) |
| Task 4 | Processing book return records | O(n) |
| Task 5 | Calculating attendance statistics | O(n) |
| Task 6 | Processing and validating registrations | O(n) average |

Here, n represents the number of records processed. These are the main processing costs; sorting, reporting and other operations may add further costs.

## 8. Requirements

The assignment uses Python built-in modules. No third-party packages are required.

Refer to `requirements.txt` for dependency information.

## 9. Conclusion

This assignment provides practical knowledge of Python file handling, exception handling, custom exceptions, modules and packages. It improves the ability to design reliable programs that process data and handle unexpected errors.

All six tasks demonstrate the application of Python programming concepts to real-world situations such as mess bill processing, biometric attendance, library records and college fest registrations.

---

**Submitted as part of CSA08 – Python Programming, Assignment 4.**
