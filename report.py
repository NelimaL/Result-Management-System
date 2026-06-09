
from logic import (
    calculate_average,
    assign_grade,
    get_top_student,
    class_average
)


def print_report(students):

    if not students:
        print("No student records found.")
        return

    print("\n========================================")
    print("      NAKURU HIGH SCHOOL REPORT")
    print("========================================")

    print(f"{'Name':20} {'Average':10} {'Grade'}")
    print("----------------------------------------")

    for student in students:

        avg = calculate_average(student)
        grade = assign_grade(avg)

        print(
            f"{student['name']:20} "
            f"{avg:<10.1f} "
            f"{grade}"
        )

    print("----------------------------------------")

    class_avg = class_average(students)

    top = get_top_student(students)
    top_avg = calculate_average(top)

    print(f"Class Average: {class_avg:.1f}")
    print(
        f"Top Student: {top['name']} ({top_avg:.1f})"
    )

    print("========================================")
