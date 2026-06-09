from file_handler import save_student, load_students
from report import print_report


def add_student():
    """
    Prompts the user to enter student details and saves them to a file.
    The function collects the student's name and marks for Maths, English, and Science.
    It validates the marks to ensure they are between 0 and 100. Once the details
    are collected and validated, the student information is saved using the save_student function.

    Parameters:
    None

    Returns:
    None
    """
    name = input("Student name: ")

    maths = get_valid_mark("Maths")
    english = get_valid_mark("English")
    science = get_valid_mark("Science")

    student = {
        "name": name,
        "maths": maths,
        "english": english,
        "science": science
    }

    save_student(student)

    print("Student saved successfully!")



def get_valid_mark(subject):
    """
    Prompts the user to enter a valid mark for a given subject. The function ensures that the mark is a number between 0 and 100. If the user enters an invalid mark, it will display an error message and prompt them to enter the mark again until a valid mark is provided.
    Parameters:
    subject (str): The name of the subject for which the mark is being entered.
    Returns:
    float: A valid mark for the specified subject.
    """
    while True:
        try:
            mark = float(input(f"Enter mark for {subject}: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Mark must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")



def view_students():
    """Loads and displays all student records from the file. The function retrieves the list of students using the load_students function and checks if any student records are found. If no records are found, it will display a message indicating that no students were found. If records are found, it will iterate through the list of students and print their details to the console.
    Parameters:    None
    Returns:    None
    """
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)



def main():
    """
    The main function to run the student results system.
    It displays a menu to the user with options to add a student, view all students, print a report, or exit the program. The function uses a while loop to continuously display the menu until the user chooses to exit. Based on the user's choice, it calls the appropriate functions to perform the desired actions.
    Parameters:    None
    Returns:    None

    """
    while True:
        print("\n=== Nakuru High School — Results System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Print Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            students = load_students()
            print_report(students)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()