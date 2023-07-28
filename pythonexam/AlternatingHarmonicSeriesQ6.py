# function defination
def series_sum(n):
    output = 0
    initial_sign = 1

    for i in range(1, n + 1):
        intermediate_value = initial_sign * (1 / i)
        output += intermediate_value
        initial_sign *= -1
    return output


n = int(input("Enter the Iteration number (n): "))
# function call
result = series_sum(n)
print(f"Sum of series for {n} iteration is: {result:.4f}")
