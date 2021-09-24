def main():
    first_number = float(input("Input first number: "))
    second_number = float(input("Input second number: "))
    third_number = float(input("Input third number: "))
    if first_number <= second_number:
        if second_number <= third_number:
            sorted_numbers = [first_number, second_number, third_number]
        elif third_number <= first_number:
            sorted_numbers = [third_number, first_number, second_number]
        else:
            sorted_numbers = [first_number, third_number, second_number]
    else:
        if first_number <= third_number:
            sorted_numbers = [second_number, first_number, third_number]
        elif third_number <= second_number:
            sorted_numbers = [third_number, second_number, first_number]
        else:
            sorted_numbers = [second_number, third_number, first_number]
    print(", ".join([str(n) for n in sorted_numbers]))


if __name__ == '__main__':
    main()
