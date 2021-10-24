def months_and_days(month):
    """
    input a Integer of number in [1, 12] and return
    corresponding month and days like following format:
    "February, 28\n"
    :param month: integer in [1, 12]
    :return: formatted month and days string
    """
    month_names = ["January", "February", "March",
                   "April", "May", "June", "July",
                   "August", "September", "October",
                   "November", "December"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_names[month - 1] + ", " + str(days[month - 1]) + "\n"


def test_months_and_days():
    """
    Test function for months_and_days
    :return: None
    """
    expected = [
        "January, 31\n",
        "February, 28\n",
        "March, 31\n",
        "April, 30\n",
        "May, 31\n",
        "June, 30\n",
        "July, 31\n",
        "August, 31\n",
        "September, 30\n",
        "October, 31\n",
        "November, 30\n",
        "December, 31\n"
    ]

    for i in range(len(expected)):
        actual = months_and_days(i + 1)
        if actual != expected[i]:
            print("Test", i + 1, "failed,\n", "expected:",
                  expected[i], "got:", actual)


if __name__ == '__main__':
    test_months_and_days()
