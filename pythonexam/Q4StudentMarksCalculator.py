def calculate_grade(final_grade):
    if 94 <= final_grade <= 100:
        return "A+"
    elif 87 <= final_grade <= 93:
        return "A"
    elif 80 <= final_grade <= 86:
        return "A-"
    elif 77 <= final_grade <= 79:
        return "B+"
    elif 73 <= final_grade <= 76:
        return "B"
    elif 70 <= final_grade <= 72:
        return "B-"
    else:
        return "No Option"


def final_grade_calculator(student_number, assignment_grade, midterm_grade, final_term_grade, project_grade):
    # Calculate the final grade based on the given weighting
    final_grade = (assignment_grade * 0.3) + (midterm_grade * 0.2) + (final_term_grade * 0.2) + (project_grade * 0.3)

    # Round the final grade to two decimal places
    final_grade = round(final_grade, 2)

    # Get the corresponding mark for the final grade
    mark = calculate_grade(final_grade)

    # Print the results
    print(f"Student Number: {student_number}")
    print(f"Final Marks: {final_grade}")
    print(f"Final Grade: {mark}")

student_number = "C04823673  "
assignment_grade = 80
midterm_grade = 70
final_term_grade = 73
project_grade = 82

final_grade_calculator(student_number, assignment_grade, midterm_grade, final_term_grade, project_grade)
