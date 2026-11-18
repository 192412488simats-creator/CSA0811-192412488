# Task 1 – File-Processing Design Review

## Assignment Details
- **Course Code:** CSA0811
- **Course Name:** Python Programming
- **Course Outcome:** CO4
- **Task:** File-Processing Design Review: Diagnose and Repair a Poor Script
- **Marks:** 6

## Objective
To identify the problems in a poorly designed Python file-processing program and develop a safer and more reliable solution.

## Concepts Used
- File handling
- Line-by-line reading
- Functions
- Exception handling
- Rejected record management

## Program File
`AT4 T1.py`

## Program Description
The program processes hostel mess bill records containing register numbers, student names and bill amounts. It calculates the total bill amount and identifies invalid records.

## Sample Input
```text
192311001,Ravi,1250.50
192311002,Arun,1400
192311003,Meena,abc
192311004,Divya,1200
```

## Expected Result
- Displays valid student bill records.
- Calculates the total bill amount.
- Identifies invalid records.
- Handles missing input files.

## Time Complexity
O(n), where n is the number of records.

## How to Execute
```bash
python AT4 T1.py
```

## Conclusion
The program demonstrates safe data processing using functions, line-by-line reading and exception handling.
