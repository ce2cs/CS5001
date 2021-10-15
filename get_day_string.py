def get_day_string():
    days = ""
    for i in range(1, 8):
        days += which_day(i) + " "
    print(days.strip())


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


if __name__ == '__main__':
    get_day_string()
