"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helper import get_all_primes_below_limit


if __name__ == '__main__':
    limit = 2000000
    primes = get_all_primes_below_limit(limit)
    print(sum(primes))
