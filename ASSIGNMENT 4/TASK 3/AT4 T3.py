
import io

class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    reg_no, date, status = parts

    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")

    return reg_no, date, status


def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        # Simulate opening a file
        if path not in virtual_files:
            raise FileNotFoundError(path)

        with io.StringIO(virtual_files[path]) as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    reg_no, date, status = parse_line(line)

                    if status == "P":
                        present += 1
                    else:
                        absent += 1

                except InvalidRecord as error:
                    errors.append((line_number, str(error)))

    except FileNotFoundError as error:
        raise RuntimeError("Attendance file not found") from error

    else:
        print("File processed successfully.")

    finally:
        print("Processing operation finished.")

    return present, absent, errors


virtual_files = {
    "attendance.csv":
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
}

try:
    result = summarise("attendance.csv")
    print(result)

except RuntimeError as error:
    print(error)

# Test missing file
try:
    summarise("missing.csv")

except RuntimeError as error:
    print("Handled error:", error)
    print("Original cause:", type(error.__cause__).__name__)
