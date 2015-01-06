"""
Problem 7 - 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

primes = [2]
limit = 10001
contor = 1
prime = 2

while contor != limit:
    prime += 1
    is_prime = True      # check that this number is prime
    for j in primes:
        if is_prime and prime%j == 0:
            is_prime = False
    if is_prime:        # if the number is prime, add it to the list
        primes.append(prime)
        # print(primes)
        contor += 1

print(primes[-1])

