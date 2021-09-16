"""
Suppose you are at the grocery store to buy soda and you want to get the best deal.
Write a program that reads in the price of a six-pack of soda and the price of a two-liter bottle.
The program should print out the price per liter for both assuming that cans are 12 oz or 0.355 liters.
For example:

Price per six-pack: 2.75
Price per two-liter: 1.74

Six-pack price per liter: 1.2910798122065728
Two-liter price per liter: 0.87
"""


def main():
    try:
        six_pack_price = float(input("Price per six-pack: "))
        two_liter_price = float(input("Price per two-liter: "))
    except ValueError as e:
        print("Please input a float number")
        return
    print("Six-pack price per liter: {}".format(six_pack_price / (0.355 * 6)))
    print("Two-liter price per liter: {}".format(two_liter_price/ 2))


if __name__ == '__main__':
    main()
