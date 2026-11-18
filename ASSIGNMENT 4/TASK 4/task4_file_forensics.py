from pathlib import Path


def save_returns_bad(books, log_name):
    # Deliberately incorrect: "w" overwrites the old file; no newline is added.
    log = open(log_name, "w", encoding="utf-8")
    for book in books:
        log.write(book)
    log.close()


def process_bad(day_file, log_name):
    try:
        books = Path(day_file).read_text(encoding="utf-8").splitlines()
        save_returns_bad(books, log_name)
    except FileNotFoundError:
        print("missing")


def save_returns_fixed(books, log_name):
    with open(log_name, "a", encoding="utf-8") as log:
        for book in books:
            log.write(book + "\n")


def process_fixed(day_file, log_name, error_log):
    try:
        with open(day_file, "r", encoding="utf-8") as file:
            books = [line.strip() for line in file if line.strip()]
        save_returns_fixed(books, log_name)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError) as error:
        with open(error_log, "a", encoding="utf-8") as log:
            log.write(f"{day_file}: {type(error).__name__}: {error}\n")
        print("Error recorded:", error)


if __name__ == "__main__":
    folder = Path("daily_returns")
    bad_log = Path("bad_returns.log")
    fixed_log = Path("returns.log")
    error_log = Path("error.log")

    # Reset demonstration output files.
    for path in (bad_log, fixed_log, error_log):
        if path.exists():
            path.unlink()

    print("BAD VERSION – each day overwrites the previous day:")
    for day in ("day1.txt", "day2.txt", "day3.txt"):
        process_bad(folder / day, bad_log)
    print(bad_log.read_text(encoding="utf-8"))
    print("Only the last day's records remain, and records have no added separators.")

    print("\nCORRECTED VERSION – append mode and newline:")
    for day in ("day1.txt", "day2.txt", "day3.txt"):
        process_fixed(folder / day, fixed_log, error_log)
    # Demonstrate missing-file handling.
    process_fixed(folder / "missing_day.txt", fixed_log, error_log)

    print("\nCorrected returns log:")
    print(fixed_log.read_text(encoding="utf-8"))
    print("Error log:")
    print(error_log.read_text(encoding="utf-8"))
