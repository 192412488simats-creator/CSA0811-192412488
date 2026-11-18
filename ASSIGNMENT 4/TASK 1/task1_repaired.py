from pathlib import Path


def create_sample_file(file_name):
    """Create a small sample input file if it is not already present."""
    path = Path(file_name)
    if not path.exists():
        sample = (
            "192311001,Anu,1250.50\n"
            "192311002,Bala,980\n"
            "192311003,Charan,abc\n"
            "192311004,Divya,1450.75\n"
            "damaged line\n"
        )
        path.write_text(sample, encoding="utf-8")


def process_mess_file(file_name):
    total = 0.0
    report_rows = []
    rejected_lines = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    parts = line.split(",")
                    if len(parts) != 3:
                        raise ValueError("expected 3 comma-separated fields")

                    register_no, name, amount_text = parts
                    amount = float(amount_text)

                    report_rows.append(f"{name} {amount:.2f}")
                    total += amount

                except (ValueError, IndexError) as error:
                    rejected_lines.append(
                        f"Line {line_number}: {line} ({error})"
                    )

    except FileNotFoundError:
        print("Error: input file not found:", file_name)
        return

    print("MESS BILL REPORT")
    for row in report_rows:
        print(row)
    print(f"Total: {total:.2f}")

    print("\nRejected lines:")
    if rejected_lines:
        for item in rejected_lines:
            print(item)
    else:
        print("None")


if __name__ == "__main__":
    input_file = "mess_oct.txt"
    create_sample_file(input_file)
    process_mess_file(input_file)
