"""
Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

limit = 1000

multiples3 = [i for i in range(limit) if i%3==0 ]
multiples5 = [i for i in range(limit) if i%5==0 ]

multiples_sum = sum(set(multiples5 + multiples3))

print(multiples3)
print(multiples5)
print(multiples_sum)

