"""
Write a program that reads a measurement in meters and the converts it to inches, feet, and miles.
There are 39.3701 inches in a meter. For example:

Enter length: 42
The length in inches is 1653.5442
The length in feet is 137.79528
The length in miles is 0.026097582
"""
METER_TO_INCHES = 39.3701
METER_TO_FEET = METER_TO_INCHES / 12
METER_TO_MILE = METER_TO_INCHES / 63360


def main():
    try:
        length = float(input("Enter length: "))
    except ValueError as e:
        print("Please input a float number")
        return
    print("The length in inches is {}".format(length * METER_TO_INCHES))
    print("The length in feet is {}".format(length * METER_TO_FEET))
    print("The length in miles is {}".format(length * METER_TO_MILE))


if __name__ == '__main__':
    main()
