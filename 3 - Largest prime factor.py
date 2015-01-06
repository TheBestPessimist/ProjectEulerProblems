"""
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""




"""
HOw to solve:
600851475143 is divisible by 3 => new nr is 
"""
from math import sqrt

def find_prime_factors(nr):
    factors = []
    for i in range(2, int(sqrt(nr))):
        if nr%i == 0:
            is_prime = True      # check that this number is prime
            for j in factors:
                if is_prime  and i%j == 0:
                    is_prime = False
            if is_prime:         # if the number is prime, add it
                factors.append(i)
                print (factors)
    return factors



if __name__ == '__main__':
    nr = 600851475143
    # nr = 13195

    factors = find_prime_factors(nr)

    print(factors)
