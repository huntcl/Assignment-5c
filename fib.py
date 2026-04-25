# Author: Clara Hunt
# Github username: huntcl
# Date: 04/24/26
# Description: Returns the nth Fibonacci number.

def fib(n):
    """Return nth Fibonacci number."""
    if n == 1 or n == 2:
        return 1

    a = 1
    b = 1

    for count in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b
