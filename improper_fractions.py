def main():
    try:
        n = float(input("Enter a floating point number: "))
        numerator = int(100 * n)
    except ValueError as e:
        print("Please enter a floating number")
        return

    print(n, "is", str(numerator) + '/100')


if __name__ == '__main__':
    main()
