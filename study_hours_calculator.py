# Name: Daniel Brito
# Summary: This program calculates how many hours a student should study
#          outside of class based on credits and desired grade.
# Date Last Updated: 03/14/2026

print("***************************************")
print("Thank you for using the Study Hours Calculator")
print("By: Daniel Brito")
print("Last Modified: 03/15/2026")
print("***************************************")

total_students = 0
total_credits = 0
total_study_hours = 0

run_program = "yes"

while run_program.lower() == "yes":
    # Get and validate full name
    full_name = input("\nPlease enter the student's full name: ").strip()

    while full_name == "":
        full_name = input("Invalid input. Please enter the student's full name: ").strip()

    full_name = full_name.title()

    # Get and validate credits
    credits_input = input(
        "Please enter the number of credits in whole numbers only "
        "(must be greater than 0 and divisible by 3): "
    ).strip()

    while not credits_input.isdigit():
        credits_input = input(
            "Invalid input. Please enter the number of credits using digits only: "
        ).strip()

    number_of_credits = int(credits_input)

    while number_of_credits <= 0 or number_of_credits % 3 != 0:
        credits_input = input(
            "Invalid input. Enter credits greater than 0 and divisible by 3: "
        ).strip()

        while not credits_input.isdigit():
            credits_input = input(
                "Invalid input. Please enter the number of credits using digits only: "
            ).strip()

        number_of_credits = int(credits_input)

    # Get and validate desired grade
    desired_grade = input(
        "Please enter the grade you want (A, B, C, D, or F): "
    ).strip().upper()

    while desired_grade not in ["A", "B", "C", "D", "F"]:
        desired_grade = input(
            "Invalid input. Please enter A, B, C, D, or F: "
        ).strip().upper()

    # Determine study hours per class using decision structure
    if desired_grade == "A":
        study_hours_per_class = 15
    elif desired_grade == "B":
        study_hours_per_class = 12
    elif desired_grade == "C":
        study_hours_per_class = 9
    elif desired_grade == "D":
        study_hours_per_class = 6
    else:
        study_hours_per_class = 0

    number_of_classes = number_of_credits // 3
    weekly_study_hours = number_of_classes * study_hours_per_class

    # Display student results
    print("\nName:", full_name)
    print("Credits:", number_of_credits)
    print("Study Hours:", weekly_study_hours)
    print("Grade:", desired_grade)

    # Update totals
    total_students += 1
    total_credits += number_of_credits
    total_study_hours += weekly_study_hours

    # Ask to continue
    run_program = input(
        "\nWould you like to enter another student? Please type yes or no: "
    ).strip().lower()

    while run_program not in ["yes", "no"]:
        run_program = input(
            "Invalid input. Please type yes or no: "
        ).strip().lower()

# Display final summary
if total_students > 0:
    average_credits = total_credits / total_students
    average_study_hours = total_study_hours / total_students

    print("\nTotal Students:", total_students)
    print("Average Credits: {:.2f}".format(average_credits))
    print("Average Study Hours: {:.2f}".format(average_study_hours))
else:
    print("\nNo student data was entered.")
