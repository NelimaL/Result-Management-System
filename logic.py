def calculate_average(student):
    total = (
        student["maths"] +
        student["english"] +
        student["science"]
    )

    return total / 3


def assign_grade(average):

    if average >= 70:
        return "A"

    elif average >= 60:
        return "B"

    elif average >= 50:
        return "C"

    elif average >= 40:
        return "D"

    else:
        return "F"


def get_top_student(students):

    if not students:
        print("Student Not in System!")

    top_student = students[0]
    highest_average = calculate_average(top_student)

    for student in students:

        avg = calculate_average(student)

        if avg > highest_average:
            highest_average = avg
            top_student = student

    return top_student


def class_average(students):

    if not students:
        return 0

    total = 0

    for student in students:
        total += calculate_average(student)

    return total / len(students)