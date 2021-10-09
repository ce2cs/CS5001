def which_day(day_integer):
    days = ["Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"]
    return days[day_integer - 1]


def main():
    if which_day(1) != "Sunday":
        print("Test Failed!\nInputs are:", 1)
    if which_day(2) != "Monday":
        print("Test Failed!\nInputs are:", 2)
    if which_day(3) != "Tuesday":
        print("Test Failed!\nInputs are:", 3)
    if which_day(4) != "Wednesday":
        print("Test Failed!\nInputs are:", 4)
    if which_day(5) != "Thursday":
        print("Test Failed!\nInputs are:", 5)
    if which_day(6) != "Friday":
        print("Test Failed!\nInputs are:", 6)
    if which_day(7) != "Saturday":
        print("Test Failed!\nInputs are:", 7)
    print("Test passed!")


if __name__ == '__main__':
    main()
