def get_day_string():
    """
    Return the days of the week as string format
    using which_day function
    :return: days of the week with space between
    """
    days = ""
    for i in range(1, 8):
        days += which_day(i) + " "
    return days.strip()


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
    Test function of get_day_string
    :return: None
    """
    expected = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
    actual = get_day_string()
    if actual == expected:
        print("Test Passed!")
    else:
        print("Test Failed!")


if __name__ == '__main__':
    main()
