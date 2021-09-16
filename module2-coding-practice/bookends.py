"""
Write a program that reads a 4-digit number from the keyboard and prints
the first and last digits of the number.
For example,

Enter number: 1234
The first number is 1
The last number is 4
"""


def main():
    try:
        n = input("Enter number: ")
        if len(n) != 4:
            raise ValueError
        int_n = int(n)
        print("The first number is {}".format(n[0]))
        print("The last number is {}".format(n[-1]))
    except ValueError as e:
        print("Please input a 4-digit number")
        return


if __name__ == '__main__':
    main()
