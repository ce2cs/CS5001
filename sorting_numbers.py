def main():
    first_number = float(input("Input first number: "))
    second_number = float(input("Input second number: "))
    third_number = float(input("Input third number: "))
    if first_number <= second_number:
        if second_number <= third_number:
            print(first_number, ",", second_number, ",", third_number)
        elif third_number <= first_number:
            print(third_number, ",", first_number, ",", second_number)
        else:
            print(first_number, ",", third_number, ",", second_number)
    else:
        if first_number <= third_number:
            print(second_number, ",", first_number, ",", third_number)
        elif third_number <= second_number:
            print(third_number, ",", second_number, ",", first_number)
        else:
            print(second_number, ",", third_number, ",", second_number)


if __name__ == '__main__':
    main()
