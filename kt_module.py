#kt_module

import math
def is_prime(num):
    """1.Check whether the given number is prime or composite."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci_series(n):
    """2.Find the Fibonacci series in the given range."""
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def factorial(num):
    """3.Find the factorial of the given number."""
    if num == 0:
        return 1
    return num * factorial(num - 1)

def sum_even_odd(start, end):
    """4.Add the even and odd numbers in the given range."""
    even_sum = sum(i for i in range(start, end + 1) if i % 2 == 0)
    odd_sum = sum(i for i in range(start, end + 1) if i % 2 != 0)
    return even_sum, odd_sum

def is_perfect_square(num):
    """5.Check whether a number is a perfect square or not."""
    return math.isqrt(num) ** 2 == num

def is_coprime(a, b):
    """6.Check whether a number is coprime or not."""
    return math.gcd(a, b) == 1

def print_pattern(rows):
    """7.Create a pattern with * symbol."""
    for i in range(1, rows + 1):
        print("*" * i)

def convert_case(string):
    """8.Convert uppercase to lowercase."""
    return string.lower()

def remove_special_characters(string):
    """9.Print the string without special characters."""
    return ''.join(e for e in string if e.isalnum())

def combinations(lst):
    """10.Find the combinations in the given list."""
    from itertools import combinations
    return list(combinations(lst, 2))

def encrypt(text, key):
    """11.Creative function for encryption."""
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def decrypt(encrypted_text, key):
    """12.Create a function for decryption."""
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text
