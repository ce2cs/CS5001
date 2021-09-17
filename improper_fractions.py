def main():
    try:
        n = float(input("Enter a floating point number: "))
        n *= 100
        n = int(n)
    except ValueError as e:
        print("Please enter a floating number")
        return

    print(n, "is", str(n) + '/100')


if __name__ == '__main__':
    main()
