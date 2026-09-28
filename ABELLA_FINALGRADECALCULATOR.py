"""
Name: Your name
Grade and Section: Grade 8 - Your section
Date: September 28, 2026
Description: Computes a student's final grade.
Reference: Teacher's instructions
"""

import math


def title():
    print("FINAL GRADE CALCULATOR")


def get_score(name, maximum):
    # Repeat until the user enters a valid score.
    while True:
        try:
            score = int(input(f"{name} (0 to {maximum}): "))
            if 0 <= score <= maximum:
                return score
            print("Score is out of range.")
        except ValueError:
            print("Enter a whole number.")


def calculate_grade(fa, lt, pt, project):
    # Add the weighted parts of the grade.
    return math.fsum([
        fa * 0.30,
        lt * 0.30,
        pt * 0.30,
        project * 0.10
    ])


def get_rating(grade):
    # Temporary cutoffs.
    if grade >= 90:
        return "EXCELLENT"
    elif grade >= 85:
        return "VERY GOOD"
    elif grade >= 80:
        return "GOOD"
    elif grade >= 75:
        return "SATISFACTORY"
    else:
        return "NEEDS IMPROVEMENT"


def show_result():
    print("\nFINAL GRADE REPORT")
    print("Name:", name)
    print("Student ID:", student_id)

    print("\nSCORES")
    print("FA 1:", fa1, "/ 30")
    print("FA 2:", fa2, "/ 30")
    print("FA 3:", fa3, "/ 25")
    print("FA 4:", fa4, "/ 30")
    print("FA 5:", fa5, "/ 20")
    print("Long Test:", lt, "/ 50")
    print("Practical Test:", pt, "/ 60")
    print("Project Proposal:", project, "/ 100")

    print("\nPERCENTAGES")
    print(f"FA: {fa_percent:.2f}% (weight: 30%)")
    print(f"Long Test: {lt_percent:.2f}% (weight: 30%)")
    print(f"Practical Test: {pt_percent:.2f}% (weight: 30%)")
    print(f"Project: {project_percent:.2f}% (weight: 10%)")

    print(f"\nFinal Grade: {grade:.2f}%")
    print("Rating:", get_rating(grade))


title()

# A name containing only spaces is not accepted.
name = input("Student name: ").strip()
while name == "":
    print("Name cannot be blank.")
    name = input("Student name: ").strip()

# Check for G8- followed by exactly four digits.
while True:
    student_id = input("Student ID (G8-1234): ").strip()
    if (student_id.startswith("G8-")
            and len(student_id) == 7
            and student_id[3:].isascii()
            and student_id[3:].isdigit()):
        break
    print("Use G8- followed by four digits.")

fa1 = get_score("FA 1", 30)
fa2 = get_score("FA 2", 30)
fa3 = get_score("FA 3", 25)
fa4 = get_score("FA 4", 30)
fa5 = get_score("FA 5", 20)
lt = get_score("Long Test", 50)
pt = get_score("Practical Test", 60)
project = get_score("Project Proposal", 100)

# Convert scores to percentages before applying the weights.
fa_percent = (fa1 + fa2 + fa3 + fa4 + fa5) / 135 * 100
lt_percent = lt / 50 * 100
pt_percent = pt / 60 * 100
project_percent = project / 100 * 100

grade = calculate_grade(
    fa_percent, lt_percent, pt_percent, project_percent
)

show_result()