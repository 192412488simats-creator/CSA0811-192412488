# Task 3 – Design the Error Handling

## Assignment Details
- **Course Code:** CSA08
- **Course Name:** Python Programming
- **Course Outcome:** CO4
- **Task:** Exceptions in the Attendance Processor
- **Marks:** 9

## Objective
To identify possible program failures and implement exception handling using built-in and custom exceptions.

## Concepts Used
- Custom exceptions
- try and except statements
- else and finally blocks
- raise statement
- raise from statement
- FileNotFoundError
- InvalidRecord exception

## Program File
`AT4 T3.py`

## Program Description
The program validates attendance records and handles invalid data using a custom exception named `InvalidRecord`. It counts present and absent records and records damaged lines.

## Expected Result
- Validates attendance records.
- Counts present and absent students.
- Identifies invalid records.
- Handles missing-file errors.
- Demonstrates exception chaining.

## Time Complexity
O(n), where n is the number of attendance records.

## How to Execute
```bash
python AT4 T3.py
```

## Conclusion
The program demonstrates reliable error handling using custom exceptions and Python exception-handling statements.
