import random


def count_by_fives(ending_value):
    result = []
    count = 0
    while count <= ending_value:
        result.append(count)
        count += 5
    return result


def count_by_fives_recursive(ending_value):
    """
    count all numbers divide by 5 smaller or equal to ending value
    :param ending_value: Integer
    :return: list of Integer
    """
    # base case
    if ending_value < 5:
        return [0]
    # count all numbers divide by 5 smaller or equal to ending value - 5
    sub_counts = count_by_fives(ending_value - 5)
    sub_counts.append(sub_counts[-1] + 5)
    return sub_counts


def test_count_by_fives_recursive():
    """
    Test function for count_by_fives_recursive
    :return: None
    """
    pass_count = 0
    cases_number = 100
    for i in range(cases_number):
        test_case = random.random() * 100
        expected = count_by_fives(test_case)
        actual = count_by_fives_recursive(test_case)
        if expected != actual:
            print("Test", i, "Failed")
            print("expected:", expected)
            print("actual:", actual)
        else:
            pass_count += 1
    print(str(pass_count) + "/" + str(cases_number), "passed")


if __name__ == '__main__':
    test_count_by_fives_recursive()
