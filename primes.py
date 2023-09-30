"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    num = 2
    while len(list) < number_of_primes:
        if all(num % prime != 0 for prime in list):
            list.append(num)
        num += 1
    return list
