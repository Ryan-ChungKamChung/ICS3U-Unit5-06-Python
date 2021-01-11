#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program rounds numbers


def rounding(numbers, decimal):
    # Rounds user input to chosen amount of decimal values

    numbers[0] = (int(numbers[0] * (10 ** decimal) + 0.5)
                  / (10 ** decimal))


def main():
    # Takes user input, passes it to functions and calls them

    numbers = []

    print("I round off numbers!")

    while True:
        number_string = input("Enter number: ")
        try:
            number = float(number_string)
            numbers.append(number)
            break
        except Exception:
            print("This isn't a valid input")
    while True:
        decimal_string = input("How many decimals would you like me "
                               "to round to? ")
        try:
            decimal = int(decimal_string)
            assert decimal > 0
            break
        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    rounding(numbers, decimal)

    print("Result: {0}".format(numbers[0]))


if __name__ == "__main__":
    main()
