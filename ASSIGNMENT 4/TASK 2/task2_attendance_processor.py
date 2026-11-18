from pathlib import Path
import csv


def process_attendance(input_folder):
    folder = Path(input_folder)
    counts = {}  # register number: [present, absent]
    damaged = []

    for file_path in sorted(folder.glob("*.txt")):
        try:
            with file_path.open("r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    text = line.strip()
                    if not text:
                        continue
                    parts = text.split(",")

                    if len(parts) != 3:
                        damaged.append(
                            f"{file_path.name}, line {line_number}: {text}"
                        )
                        continue

                    register_no, date, status = parts
                    if status not in ("P", "A") or not register_no or not date:
                        damaged.append(
                            f"{file_path.name}, line {line_number}: {text}"
                        )
                        continue

                    counts.setdefault(register_no, [0, 0])
                    if status == "P":
                        counts[register_no][0] += 1
                    else:
                        counts[register_no][1] += 1

        except (OSError, UnicodeDecodeError) as error:
            damaged.append(f"{file_path.name}: FILE ERROR: {error}")

    output_folder = Path(".")
    with (output_folder / "attendance_percentages.csv").open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Register Number", "Present", "Absent", "Percentage"])
        for register_no, (present, absent) in sorted(counts.items()):
            total = present + absent
            percentage = (present / total * 100) if total else 0
            writer.writerow([register_no, present, absent, f"{percentage:.2f}"])

    with (output_folder / "below_75_percent.txt").open(
        "w", encoding="utf-8"
    ) as file:
        for register_no, (present, absent) in sorted(counts.items()):
            total = present + absent
            percentage = (present / total * 100) if total else 0
            if percentage < 75:
                file.write(f"{register_no}: {percentage:.2f}%\n")

    with (output_folder / "damaged_records.log").open(
        "w", encoding="utf-8"
    ) as file:
        for item in damaged:
            file.write(item + "\n")

    print("Attendance processing completed.")
    print("Students processed:", len(counts))
    print("Created: attendance_percentages.csv")
    print("Created: below_75_percent.txt")
    print("Created: damaged_records.log")


if __name__ == "__main__":
    process_attendance("input")
