"""
Highly divisible triangular number
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


from helper import get_all_factors_of_n


def main():
    nr = 1
    triangle = 1
    # div2 = 1

    while True:
        nr += 1
        triangle += nr
        divisors_no = len(get_all_factors_of_n(triangle))
        if divisors_no > 500:
            print("triangle: ", triangle, divisors_no, nr)
            break
        # if divisors_no/100 >= 1:
            # print("many divisors: ", triangle, nr, divisors_no)
        # if triangle / (1000000*div2) >= 1:
        #     print("1kk ", triangle, nr)
        #     div2 += 1


if __name__ == '__main__':
    main()