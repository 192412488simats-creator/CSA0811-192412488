# Task 4 – File and Exception Forensics

## Assignment Details
- **Course Code:** CSA08
- **Course Name:** Python Programming
- **Course Outcome:** CO4
- **Task:** File and Exception Forensics
- **Marks:** 7

## Objective
To identify file-handling defects and correct them using suitable file modes and exception handling.

## Concepts Used
- File opening modes
- Append mode
- Newline characters
- with statement
- Error logging
- FileNotFoundError

## Program File
`AT4 T4.py`

## Program Description
The program processes returned book records from three different days. It combines the records into a single log and records missing-file errors separately.

## Expected Result
- Processes book return records from three days.
- Preserves previous records using append mode.
- Displays records on separate lines.
- Handles missing files.
- Maintains an error log.

## Time Complexity
O(n), where n is the number of returned book records.

## How to Execute
```bash
python AT4 T4.py
```

## Conclusion
The program demonstrates proper file handling using append mode, context managers and exception handling.
