"""
Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""



nr = 20
is_multiple = False

while(not is_multiple):
    nr += 1
    for i in range(1, 10):
        if nr % i is not 0:
            is_multiple = False
            break
        else:
            is_multiple = True

print (nr)


"""
4           = 2 2
6           = 2 3
8           = 2 2 2
7           = 7
9           = 3 3
10          = 2 5
11          = 11 
12          = 2 2 3 
13          = 13
16          = 2 2 2 2
17          = 17
18          = 2 3 3
19          = 19
20          = 2 2 5

=> 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
"""
