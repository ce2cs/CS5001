def atm():
    """
    This function simulates the behavior of an ATM
    it receives a withdraw number from stdin and
    print the cashes
    :return: None
    """
    withdraw = float(input("Input request: "))
    withdraw = round(withdraw, 2)
    withdraw *= 100
    withdraw = int(withdraw)
    # prepare all constants
    cash_number = [5000, 2000, 1000, 500, 200, 100, 25, 10, 5]
    cash_name_single = ['fifty', 'twenty', 'ten', 'five',
                        'toony', 'loony', 'quarter', 'dime', 'nickel']
    cash_name_plural = ['fifties', 'twenties', 'tens', 'fives',
                        'toonies', 'loonies', 'quarters', 'dimes', 'nickels']
    cash_count = []

    for i in range(len(cash_number)):
        cash_count.append(withdraw // cash_number[i])
        withdraw %= cash_number[i]

    if withdraw >= 3:
        cash_count[-1] += 1

    for i in range(len(cash_number)):
        if cash_count[i] > 1:
            print(str(cash_count[i]) + " " + cash_name_plural[i])
        elif cash_count[i] > 0:
            print(str(cash_count[i]) + " " + cash_name_single[i])


def main():
    atm()


if __name__ == '__main__':
    main()
