hours = float(input("Enter the hours worked :"))
rate = 22.25


def calculate_salary():
    return hours * rate * 4


def calculate_tax(salary):
    tax = 0.13 * salary
    return tax


salary = calculate_salary()
print("Salary {0} and tax {1}".format(salary, calculate_tax(salary)))


def calculate_net():
    tax = calculate_tax(salary)
    net_pay = salary - tax
    return net_pay


print("Net salary is {}".format(calculate_net()))
