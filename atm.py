def atm(withdraw):
    withdraw = float(withdraw)
    withdraw = round(withdraw, 2)
    withdraw *= 100
    withdraw = int(withdraw)
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

    res = ""
    for i in range(len(cash_number)):
        if cash_count[i] > 1:
            res += str(cash_count[i]) + " " + cash_name_plural[i] + "\n"
        elif cash_count[i] > 0:
            res += str(cash_count[i]) + " " + cash_name_single[i] + "\n"
    return res


def main():
    with open('atm_tests.txt') as f:
        curr_input = None
        curr_expect = ""
        case_idx = 0
        for line in f.readlines():
            if line.startswith("Input request:"):
                if curr_input:
                    curr_got = atm(curr_input)
                    if curr_got == curr_expect:
                        print("Test", case_idx, "passed")
                    else:
                        print("Test", case_idx, "failed")
                        print("Expected:\n" + curr_expect)
                        print("Got:\n" + curr_got)
                    case_idx += 1
                curr_input = line[15:]
                curr_expect = ""
            else:
                curr_expect += line

        curr_got = atm(curr_input)
        if curr_got == curr_expect:
            print("Test", case_idx, "passed")
        else:
            print("Test", case_idx, "failed")
            print("Expected:\n" + curr_expect)
            print("Got:\n" + curr_got)


if __name__ == '__main__':
    main()
