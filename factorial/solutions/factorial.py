# This function computes the factorial of the given number.
# ie: fact(7) = 7! = 5040
def fact(n):
    prod = 1
    for i in range(1,(n+1)):
        prod *= i
    return prod
