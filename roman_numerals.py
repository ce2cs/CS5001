def main():
    try:
        input_n = int(input("Enter number:"))
    except ValueError as e:
        print("Please enter a integer")
        return

    res = ""
    n = input_n

    res += "M" * (n // 1000)
    n %= 1000

    res += "D" * (n // 500)
    n %= 500

    res += "C" * (n // 100)
    n %= 100

    res += "L" * (n // 50)
    n %= 50

    res += "X" * (n // 10)
    n %= 10

    res += "V" * (n // 5)
    n %= 5

    res += "I" * n

    print(input_n, "is", res)


if __name__ == '__main__':
    main()
