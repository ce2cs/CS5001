"""
Write a program that prompts with "Enter value: " and reads in an integer value from the keyboard
and prints the appropriate message depending upon the value of that input according to the following table:

Even or odd     Value           Message
Even            negative        "even negative number"
Even (and 0)    positive	    "even positive number"
Odd	            negative	    "odd negative number"
Odd	            positive	    "odd positive number"

Hint: Recall that numbers are even if they divide evenly by 0.
"""


def main():
    try:
        n = int(input("Enter value: "))
    except ValueError as e:
        print("Please input a integer number")
        return
    if n % 2 == 0 and n < 0:
        print("even negative number")
    elif n % 2 == 0 and n >= 0:
        print("even positive number")
    elif n % 2 == 1 and n < 0:
        print("odd negative number")
    else:
        print("odd positive number")


if __name__ == '__main__':
    main()
