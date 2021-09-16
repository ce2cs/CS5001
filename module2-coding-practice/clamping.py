"""
Write a program that reads in a number from the keyboard.
Your program should ensure that the value entered
is between 1 and 100 by clamping it and then print it to the screen.
Clamping a number means that any value less than the lowest value
is set to the lowest value and that any value larger than the largest
value is set to the largest value.

Examples:

Enter value: 103
Too big, clamping required
Value is 100

Enter value: -12
Too small, clamping required
Value is 1

Enter value: 42
Value is 42
"""


def main():
    try:
        n = float(input("Enter value: "))
    except ValueError as e:
        print("Please input a number")
        return

    if n > 100:
        print("Too big, clamping required")
        print("Value is 100")
    elif n < 1:
        print("Too small, clamping required")
        print("Value is 1")
    else:
        print("Value is {}".format(n))


if __name__ == '__main__':
    main()
