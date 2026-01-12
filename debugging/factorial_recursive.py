#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively calculates the factorial of a non-negative integer n.
        The factorial of 0 is defined as 1. For n > 0, factorial(n) = n * factorial(n-1).

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given integer n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Get the number from command-line argument, convert to integer, and calculate factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)

