"""
Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


palindromes = []
limit = 999


for i in range(limit, 800, -1):
    for j in range(limit, 800, -1):
        product = i * j
        is_palindrome = (str(product) == str(product)[::-1])
        if is_palindrome:
            palindromes.append(product)

sorted(palindromes)
print(palindromes[0])
