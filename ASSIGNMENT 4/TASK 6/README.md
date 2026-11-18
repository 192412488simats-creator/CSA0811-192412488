# Task 6 – College Fest Registration Desk

## Assignment Details
- **Course Code:** CSA08
- **Course Name:** Python Programming
- **Course Outcome:** CO4
- **Task:** Design Challenge – College Fest Registration Desk
- **Marks:** 13

## Objective
To design a registration processing system that validates student information, detects duplicate registrations and generates event-wise reports.

## Concepts Used
- File handling
- Dictionaries
- Duplicate detection
- String validation
- Exception handling
- Error logging
- Report generation

## Program File
`AT4 T6.py`

## Program Description
The program processes college fest registration records from different departments. It validates e-mail addresses, detects duplicate register numbers, identifies damaged records and groups participants according to their selected events.

## Expected Result
- Creates a clean master student list.
- Detects duplicate registrations.
- Validates e-mail addresses.
- Identifies damaged records.
- Generates event-wise participant lists.
- Produces a summary report.
- Records missing department files in the error log.

## Time Complexity
O(n) average for processing registrations using dictionary-based duplicate detection, where n is the number of registrations.

## How to Execute
```bash
python AT4 T6.py
```

## Conclusion
The program demonstrates a robust data-processing solution for a college fest registration system using Python.
