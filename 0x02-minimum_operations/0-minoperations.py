#!/usr/bin/python3
"""Minimum operations module."""


def minOperations(n):
    """Calculate the fewest number of operations to get n H characters.

    Returns 0 if n is impossible (e.g., n <= 1).
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
