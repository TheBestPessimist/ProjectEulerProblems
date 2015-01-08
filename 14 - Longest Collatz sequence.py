"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

limit = 1000000
# limit = 13 +1
nr = 0
max_prev = 0

for i in range(limit):
    n = i
    max_curr = 1
    while n > 1:
        n = n//2 if n%2 == 0 else 3*n+1
        max_curr += 1
    if max_curr > max_prev:
        nr, max_prev = i, max_curr
        print("i is {}, max_curr is {}".format(i, max_curr))


print(nr, max_prev)


