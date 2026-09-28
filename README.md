# ABELLA_FINAL_GRADE_CALCULATOR
FINAL GRADE CALCULATOR

Description
This is a Grade 8 CS2 project made using Python. It asks for a
student's name, ID, and assessment scores, then calculates the
final grade and displays a rating.

How to Run
1. Save the code as grade_calculator.py.
2. Open and run it using Python 3.
3. Enter your name and student ID, such as G8-1025.
4. Enter your scores when asked.
5. The program will display your grade report.

Grade Calculation
- Formative Assessments: 30%
- Long Test: 30%
- Practical Test: 30%
- Initial Project Proposal: 10%

The five FA scores are added together out of 135 points.
Each component is converted to a percentage and multiplied
by its weight. The results are added to get the final grade.

Input Validation
- The student's name cannot be blank.
- The ID must be G8- followed by four digits.
- Scores must be whole numbers within the allowed range.
- Invalid entries show an error and let the user try again.

Functions
- title(): Displays the title.
- get_score(): Gets and checks a score.
- calculate_grade(): Calculates the final weighted grade.
- get_rating(): Determines the rating.
- show_result(): Displays the complete report.

Note
The rating ranges in the code are temporary and must be checked
with the teacher. The program displays grades to two decimal
places but uses the unrounded grade to determine the rating.

References and Assistance
- Teacher's Q1_AA1 project instructions.
