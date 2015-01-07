"""
Helper functions, which are used a lot in solving the problems.
"""


def get_first_n_primes(limit):
    """
    Get the first [limit] primes.
    """

    from math import sqrt
    primes = [2]
    contor = 1
    prime = 1

    while contor != limit:
        prime += 2
        is_prime = True      # check that this number is prime
        for j in primes:
            if is_prime and prime%j == 0:
                is_prime = False
                break
            if sqrt(prime) <= j:
                break
        if is_prime:        # if the number is prime, add it to the list
            primes.append(prime)
            contor += 1
    return primes


def get_all_primes_below_limit(limit):
    """
    Get all the primes below [limit].
    """

    from math import sqrt
    primes = [2]
    prime = 1

    while prime < limit:
        prime += 2
        is_prime = True      # check that this number is prime
        for j in primes:
            if is_prime and prime%j == 0:
                is_prime = False
                break
            if sqrt(prime) <= j:
                break
        if is_prime and prime < limit:        # if the number is prime, add it to the list
            primes.append(prime)
    return primes


def list_product(l):
    """
    Python doesn't have a builtin product for lists."""
    import operator
    from functools import reduce
    return reduce(operator.mul, l, 1)
