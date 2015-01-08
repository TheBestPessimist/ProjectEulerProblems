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
    Python doesn't have a builtin product for lists.
    """
    import operator
    from functools import reduce
    return reduce(operator.mul, l, 1)


def get_all_prime_factors_of_n(n, primes):
    """
    Get all the prime factors in a number [n].
    Need a list of [primes] numbers, and the user must estimate how
        big the list should be.
    """
    factors = []
    if n in primes:
        return 2

    for prime in primes:
        while n % prime == 0 and n > 1:
            n = n // prime
            factors.append(prime)

        if n == 1:
            return factors


def get_all_factors_of_n(n):
    """
    Return a list containing all the factors of a number n.

    Taken from here: http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    from math import sqrt
    from functools import reduce
    step = 2 if n % 2 else 1  # for odd numbers, i dont need to divide by 2. It is faster!
    return set(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
