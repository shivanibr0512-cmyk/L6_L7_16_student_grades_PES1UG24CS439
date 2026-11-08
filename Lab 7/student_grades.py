def average_marks(marks_csv):
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        raise ValueError("Marks cannot be empty")

    try:
        marks = [int(m.strip()) for m in marks_csv.split(',')]
    except ValueError:
        raise ValueError("Marks must be valid integers")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    return round(sum(marks) / len(marks), 2)


def parse_srn(srn):
    if not isinstance(srn, str):
        raise ValueError("SRN must be a string")

    if (len(srn) != 13 or
        not srn[:4].isalnum() or
        srn[4:6] != "UG" or
        not srn[6:8].isdigit() or
        not srn[8:10].isalpha() or
        not srn[10:].isdigit()):
        raise ValueError("Invalid SRN")

    return srn[:4], int(srn[6:8]), srn[8:10]


def short_name(full_name):
    if not isinstance(full_name, str):
        raise ValueError("Name must be a string")

    parts = full_name.split()

    if len(parts) != 2 or not all(part.isalpha() for part in parts):
        raise ValueError("Enter exactly two alphabetic names")

    first, last = parts
    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    try:
        user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
        print("Average Marks:", average_marks(user_input))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running parse_srn ====")
    try:
        user_input = input("Enter an SRN (e.g. PES1UG24CS439): ")
        print("Campus, Year and Dept:", parse_srn(user_input))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running short_name ====")
    try:
        user_input = input("Enter first and last name (e.g. ravi kumar): ")
        print("Short Name:", short_name(user_input))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
