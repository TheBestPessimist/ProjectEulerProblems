"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

if __name__ == '__main__':
    limit = 600    # i dont think any of the numbers is greater than this
    for a in range(limit):
        for b in range(a+1, limit):
            for c in range(b+1, limit):
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    print("a: {0:<3} b: {1:<3} c: {2:<3} sum: {3:<7} prod: {4:<7}".format(a, b, c, a+b+c, a*b*c))
