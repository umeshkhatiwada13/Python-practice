class Addition:
    def add(self, num1, num2):
        return num1 + num2


class Subtraction:
    def subtract(self, num1, num2):
        return num1 - num2


class Multiplication:
    def multiply(self, num1, num2):
        return num1 * num2


class Division:
    def divide(self, num1, num2):
        return num1 / num2


class Simplify:
    @staticmethod
    def simplify():
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        # Create instances of the operation classes]
        print("Sum:", Addition().add(num1, num2))
        print("Difference:", Subtraction().subtract(num1, num2))
        print("Product:", Multiplication().multiply(num1, num2))
        print("Quotient:", Division().divide(num1, num2))


if __name__ == "__main__":
    Simplify.simplify()
