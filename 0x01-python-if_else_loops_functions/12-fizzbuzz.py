#!/usr/bin/python3
# Author - Godswill Kalu
"""print the numbers from 1 to100 separated by space.
For multiples of three,Fizz instead of the number
For multiples of five,print Buzz instead  of the number.
For multiples of three and five, print FizzBuzz instead of the number.
"""


def fizzbuzz():
    for number in range(1,101):
        if number % 3 == and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
