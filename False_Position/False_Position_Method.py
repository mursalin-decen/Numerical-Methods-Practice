import math
def f(x):
    return eval(function)


print("FALSE POSITION METHOD")

function = input("Enter the function f(x): ")

a = float(input("Enter the lower value (a): "))
b = float(input("Enter the upper value (b): "))

tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter maximum number of iterations: "))


# Check whether root exists
if f(a) * f(b) > 0:
    print("False Position method cannot be applied.")
    print("f(a) and f(b) must have opposite signs.")

else:
    print("\nIteration\t a\t\t b\t\t c\t\t f(c)")
    print("-" * 70)

    for i in range(1, max_iterations + 1):

        # False Position formula
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(i, "\t\t", round(a, 6), "\t", round(b, 6),
              "\t", round(c, 6), "\t", round(f(c), 6))

        # Check if root is found
        if abs(f(c)) < tolerance:
            print("\nRoot =", round(c, 6))
            print("Number of iterations =", i)
            break

        # Select the interval containing root
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    else:
        print("\nApproximate Root =", round(c, 6))
        print("Maximum number of iterations reached.")