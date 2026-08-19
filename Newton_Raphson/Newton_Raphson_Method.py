import math
def f(x):
    return eval(function)


def derivative(x):
    h = 0.000001
    return (f(x + h) - f(x - h)) / (2 * h)


print("NEWTON-RAPHSON METHOD")

function = input("Enter the function f(x): ")

x = float(input("Enter the initial guess (x0): "))

tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter maximum number of iterations: "))


print("\nIteration\t x\t\t f(x)")
print("-" * 50)

for i in range(1, max_iterations + 1):

    fx = f(x)
    dfx = derivative(x)

    print(i, "\t\t", round(x, 6), "\t", round(fx, 6))

    # Check if root is found
    if abs(fx) < tolerance:
        print("\nRoot =", round(x, 6))
        print("Number of iterations =", i)
        break

    # Check derivative
    if abs(dfx) < 0.0000001:
        print("\nNewton-Raphson method cannot continue.")
        print("Derivative is too close to zero.")
        break

    # Newton-Raphson formula
    x = x - (fx / dfx)

else:
    print("\nApproximate Root =", round(x, 6))
    print("Maximum number of iterations reached.")