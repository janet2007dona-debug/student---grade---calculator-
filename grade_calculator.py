"""Student Grade Calculator - handles many students."""


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "F"


def read_int(prompt, low=None, high=None):
    """Keep asking until a valid integer (within range) is entered."""
    while True:
        try:
            value = int(input(prompt))
            if (low is not None and value < low) or (high is not None and value > high):
                print(f"  Enter a number between {low} and {high}.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Enter a whole number.")


def read_marks(subject):
    while True:
        try:
            marks = float(input(f"  Marks in {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("  Marks must be between 0 and 100.")
        except ValueError:
            print("  Invalid input. Enter a number.")


def add_students(students, subjects):
    count = read_int("How many students do you want to add? ", low=1)
    for i in range(1, count + 1):
        print(f"\n--- Student {i} of {count} ---")
        name = input("Name: ").strip() or f"Student{i}"
        marks = {subject: read_marks(subject) for subject in subjects}
        total = sum(marks.values())
        percentage = total / len(subjects)
        students.append({
            "name": name,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "grade": get_grade(percentage),
            "result": "Pass" if all(m >= 40 for m in marks.values()) else "Fail",
        })
    print(f"\n{count} student(s) added.")


def show_report(students):
    if not students:
        print("\nNo students yet.")
        return
    ranked = sorted(students, key=lambda s: s["percentage"], reverse=True)
    print("\n" + "=" * 62)
    print(f"{'Rank':<6}{'Name':<16}{'Total':>8}{'%':>8}{'Grade':>8}{'Result':>9}")
    print("=" * 62)
    for rank, s in enumerate(ranked, 1):
        print(f"{rank:<6}{s['name']:<16}{s['total']:>8.1f}{s['percentage']:>8.2f}"
              f"{s['grade']:>8}{s['result']:>9}")
    print("=" * 62)


def show_summary(students):
    if not students:
        print("\nNo students yet.")
        return
    percentages = [s["percentage"] for s in students]
    topper = max(students, key=lambda s: s["percentage"])
    lowest = min(students, key=lambda s: s["percentage"])
    passed = sum(1 for s in students if s["result"] == "Pass")
    print("\n--- Class Summary ---")
    print(f"Total students : {len(students)}")
    print(f"Class average  : {sum(percentages) / len(percentages):.2f}%")
    print(f"Topper         : {topper['name']} ({topper['percentage']:.2f}%)")
    print(f"Lowest         : {lowest['name']} ({lowest['percentage']:.2f}%)")
    print(f"Passed / Failed: {passed} / {len(students) - passed}")


def search_student(students):
    name = input("Enter name to search: ").strip().lower()
    found = [s for s in students if name in s["name"].lower()]
    if not found:
        print("No student found.")
        return
    for s in found:
        print(f"\n{s['name']}")
        for subject, m in s["marks"].items():
            print(f"  {subject:<12}: {m}")
        print(f"  Total: {s['total']:.1f} | {s['percentage']:.2f}% | "
              f"Grade {s['grade']} | {s['result']}")


def main():
    print("=== Student Grade Calculator ===")
    n = read_int("How many subjects? ", low=1)
    subjects = [input(f"Name of subject {i + 1}: ").strip() or f"Subject{i + 1}"
                for i in range(n)]
    students = []

    while True:
        print("\n1. Add students\n2. Show report (ranked)\n3. Class summary"
              "\n4. Search student\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_students(students, subjects)
        elif choice == "2":
            show_report(students)
        elif choice == "3":
            show_summary(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
