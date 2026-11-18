# Task 2 – Biometric Attendance File Processing

## Assignment Details
- **Course Code:** CSA08
- **Course Name:** Python Programming
- **Course Outcome:** CO4
- **Task:** From Requirement to File-Processing Design: Biometric Attendance Files
- **Marks:** 8

## Objective
To process biometric attendance records and calculate the monthly attendance percentage of students.

## Concepts Used
- File handling
- Dictionaries
- Attendance calculation
- Exception handling
- Error logging

## Program File
`AT4 T2.py`

## Program Description
The program processes daily attendance records containing register numbers, dates and attendance status. It calculates attendance percentages and identifies students below 75%.

## Sample Input
```text
192311001,2026-10-01,P
192311002,2026-10-01,A
192311003,2026-10-01,P
```

## Expected Result
- Calculates student attendance percentages.
- Identifies students below 75% attendance.
- Detects damaged attendance records.
- Displays an error report.

## Time Complexity
O(n), where n is the total number of attendance records.

## How to Execute
```bash
python AT4 T2.py
```

## Conclusion
The program demonstrates attendance analysis using dictionaries, file processing and exception handling.
