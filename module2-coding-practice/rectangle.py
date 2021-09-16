"""
Filename: rectangle.py

Write a program that reads the length of a rectangle's sides and then prints

the area and perimeter of the rectangle

the length of the diagonal (use the Pythagorean theorem)

Hint: you can calculate the square root of a number by raising it to the 0.5 power. For example:

Enter width: 9
Enter height: 3
The area of the rectangle is 27.0
The perimeter of the rectangle is 24.0
The diagonal is 9.486832980505138
"""
import math


def main():
    try:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

    except ValueError as e:
        print("Please input a float number")
        return

    area = width * height
    perimeter = 2 * (width + height)
    diagonal = math.sqrt(width ** 2 + height ** 2)
    print("The area of the rectangle is {}".format(area))
    print("The perimeter of the rectangle is {}".format(perimeter))
    print("The diagonal is {}".format(diagonal))


if __name__ == '__main__':
    main()
