import random


def filter_list(numbers, threshold):
    """
    get numbers greater than threshold recursively
    :param numbers: list of Integers
    :param threshold: Integer
    :return: filtered list
    """
    # base case
    if len(numbers) == 0:
        return []

    # add the first number if it is greater than threshold
    if numbers[0] > threshold:
        return [numbers[0]] + filter_list(numbers[1:], threshold)
    # filter other numbers
    else:
        return filter_list(numbers[1:], threshold)


def test_filter_list():
    """
    Test function for filter_list
    :return: None
    """
    test_case_numbers = [int(random.random() * 100) for _ in range(100)]
    test_case_threshold = 50
    expected = list(filter(lambda x: x > test_case_threshold,
                           test_case_numbers))
    actual = filter_list(test_case_numbers, test_case_threshold)
    if expected != actual:
        print("Test failed")
        print("expected:", expected)
        print("actual:", actual)
    else:
        print("Test passed")


if __name__ == '__main__':
    test_filter_list()
