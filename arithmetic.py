def main():
    first_number = input("Input first number: ")
    first_number_float = float(first_number)
    second_number = input("Input second number: ")
    second_number_float = float(second_number)
    operator = input("Input operator (+,-,*,/): ")
    if operator == "+":
        res = first_number_float + second_number_float
    elif operator == "-":
        res = first_number_float - second_number_float
    elif operator == "*":
        res = first_number_float * second_number_float
    elif operator == "/":
        res = first_number_float / second_number_float
    else:
        print("Invalid operator. Please use +,-,*,/.")
        return
    print(first_number, operator, second_number, "=", res)


if __name__ == '__main__':
    main()
