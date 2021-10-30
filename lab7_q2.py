import random


def count_by_fives(ending_value):
    result = []
    count = 0
    while count <= ending_value:
        result.append(count)
        count += 5
    return result


def count_by_fives_recursive_two(current_value, ending_value):
    """
    count all numbers divide by 5 smaller or equal to ending value
    :param current_value: current value of number that can be
    divide by 5 start from 0
    :param ending_value: Integer
    :return: list of Integer
    """
    # base case
    if current_value > ending_value:
        return []

    # concatenate the result of current problem and sub problem
    return [current_value] + count_by_fives_recursive_two(
        current_value + 5, ending_value)


def test_count_by_fives_recursive_two():
    """
    Test function for count_by_fives_recursive_two
    :return: None
    """
    pass_count = 0
    cases_number = 100
    for i in range(cases_number):
        test_case = random.random() * 100
        expected = count_by_fives(test_case)
        actual = count_by_fives_recursive_two(0, test_case)
        if expected != actual:
            print("Test", i, "Failed")
            print("expected:", expected)
            print("actual:", actual)
        else:
            pass_count += 1
    print(str(pass_count) + "/" + str(cases_number), "passed")


if __name__ == '__main__':
    test_count_by_fives_recursive_two()
