import csv
import os


FILE_NAME = "students.csv"


def save_student(student):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["name", "maths", "english", "science"]
            )

        writer.writerow([
            student["name"],
            student["maths"],
            student["english"],
            student["science"]
        ])


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append({
                    "name": row["name"],
                    "maths": float(row["maths"]),
                    "english": float(row["english"]),
                    "science": float(row["science"])
                })

    except FileNotFoundError:
        print("File Not Found!")

    return students