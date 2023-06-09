def result():
    math_marks = float(input("Enter your marks in Math : "))
    science_marks = float(input("Enter your marks in Science : "))
    english_marks = float(input("Enter your marks in English : "))
    is_pass(math_marks, science_marks, english_marks)
    calculate_result(math_marks, science_marks, english_marks)


def is_pass(math_marks, science_marks, english_marks):
    if math_marks > 40 and science_marks > 40 and english_marks > 40:
        return print("Congratulations! Pass")
    else:
        return print("Fail. Better Luck next time.")


def calculate_result(math_marks, science_marks, english_marks):
    total_marks = math_marks + science_marks + english_marks
    percentage = total_marks / 3
    print("Total Marks {0} and percentage : {1}".format(total_marks, percentage))

result()
