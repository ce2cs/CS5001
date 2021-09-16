"""
Write a program that reads four integers from the keyboard and prints "two pairs"
if the input consists of two matching pairs (in some order) and "not two pairs" otherwise. For example,

1 2 2 1   two pairs
1 2 2 3   not two pairs
2 2 2 2   two pairs
"""


def main():
    try:
        four_integers = input()
        four_integers_list = four_integers.split(" ")
        four_integers_list = map(lambda i: int(i), four_integers_list)

    except Exception as e:
        print("Please input a four integers divide by single space in one line")
        return

    viewed = set()

    for i in four_integers_list:
        if i not in viewed:
            viewed.add(i)

    if len(viewed) <= 2:
        print("two pairs")
    else:
        print("not two pairs")


if __name__ == '__main__':
    main()
