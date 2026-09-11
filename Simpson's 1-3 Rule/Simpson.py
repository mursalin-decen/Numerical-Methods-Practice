import math

def f(x):
    return eval(function)

print("SIMPSON'S 1/3 RULE")

function = input("Enter the function f(x): ")

a = float(input("Enter the lower limit (a): "))
b = float(input("Enter the upper limit (b): "))
n = int(input("Enter the number of intervals (n): "))

if n % 2 != 0:
    print("\nError: Number of intervals (n) must be even.")

else:
    h = (b - a) / n

    sum_value = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            sum_value += 2 * f(x)
        else:
            sum_value += 4 * f(x)

    result = (h / 3) * sum_value

    print("\nStep size (h) =", h)
    print("Integral value =", round(result, 6))