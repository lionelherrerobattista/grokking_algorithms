#factorial function - recursion
def fact(x):
    if x == 1: #base case
        return 1
    else: #recursive case
        return x * fact(x-1)

print("Factorial of 3 - Result: " + str(fact(3)))