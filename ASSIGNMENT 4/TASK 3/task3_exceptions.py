class InvalidRecord(Exception):
    """Raised when an attendance line is not in the expected format."""


def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")

    register_no, date, status = parts
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    return register_no, date, status


def summarise(path):
    present, absent, errors = 0, 0, []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    register_no, date, status = parse_line(line)
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
                except InvalidRecord as error:
                    errors.append((line_number, str(error)))

    except FileNotFoundError as error:
        raise RuntimeError(f"Attendance file not found: {path}") from error
    except PermissionError as error:
        raise RuntimeError(f"Permission denied: {path}") from error
    except UnicodeDecodeError as error:
        raise RuntimeError(f"File encoding is not UTF-8: {path}") from error
    else:
        print("File processed successfully.")
    finally:
        print("Attendance processing attempt finished.")

    return present, absent, errors


if __name__ == "__main__":
    sample_file = "attendance_sample.csv"
    try:
        print(summarise(sample_file))
    except RuntimeError as error:
        print("Processing error:", error)
        print("Original cause:", repr(error.__cause__))

    print("\nMissing-file test:")
    try:
        print(summarise("file_that_does_not_exist.csv"))
    except RuntimeError as error:
        print("Handled:", error)
        print("Original cause:", type(error.__cause__).__name__)
