#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the argument from the command line, convert it to an integer,
# and calculate its factorial using the recursive function.
f = factorial(int(sys.argv[1]))
print(f)
