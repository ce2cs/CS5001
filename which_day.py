def which_day(day_integer):
    """
    Return the day of the week of input integer
    :param day_integer: day indicator
    :return: String format of day of the week
    """
    # store the days of the week as a list of strings
    days = ["Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"]
    # note: list index start from 0
    return days[day_integer - 1]


def main():
    """
    Test function of which_day
    :return: None
    """
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
