import math

def f(x):
    return eval(function)

print("TRAPEZOIDAL RULE")

function = input("Enter the function f(x): ")

a = float(input("Enter the lower limit (a): "))
b = float(input("Enter the upper limit (b): "))
n = int(input("Enter the number of intervals (n): "))

h = (b - a) / n

sum_value = f(a) + f(b)

for i in range(1, n):
    x = a + i * h
    sum_value += 2 * f(x)

result = (h / 2) * sum_value

print("\nStep size (h) =", h)
print("Integral value =", round(result, 6))