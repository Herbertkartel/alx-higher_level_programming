#!/usr/bin/python3
# 9-print_last_digit.py
# Bayo Herbert <herbzkartel2@gmail.com>


def print_last_digit(number):
"""Print the last digit of a number and return it."""
print(abs(number) % 10, end="")
return (abs(number) % 10)
