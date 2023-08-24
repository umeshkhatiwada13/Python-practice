import math

def estimate_pi():
    k = 0
    output = 0
    while True:
        nume = math.factorial(4*k) * (1103 + 26390*k)
        deno = (math.factorial(k)**4) * 396**(4*k)
        term = nume / deno
        output += term
        if term < 1e-15:
            break
        k += 1

    return 1 / (2 * math.sqrt(2) * output / 9801)


print(f"Estimated value of π until 10 power -15: {estimate_pi():.15f}")
