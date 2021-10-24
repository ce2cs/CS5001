import random


def find_smallest(list_of_numbers):
    '''
    find_smallest takes a list of numbers
    and returns the smallest value in the list
    :param list_of_numbers: A list of any numbers, of any size
    :return: the smallest value in list_of_numbers
    '''
    smallest = list_of_numbers[0]
    for i in range(1, len(list_of_numbers)):
        if smallest < list_of_numbers[i]:
            smallest = list_of_numbers[i]
    return smallest


def test_find_smallest():
    """
    Test function of find_smallest
    :return: None
    """
    test_case1 = [random.random() * 100] * 50
    test_case2 = [(random.random() - 0.5) * 100] * 50
    # get value by built-in method
    expected1 = min(test_case1)
    expected2 = min(test_case2)
    actual1 = find_smallest(test_case1)
    if actual1 != expected1:
        print("Test 1 failed, expected:", expected1,
              "got:", actual1,
              "input:", test_case1)
    else:
        print("Test 1 passed")

    actual2 = find_smallest(test_case2)
    if actual2 != expected2:
        print("Test 2 failed, expected:", expected2,
              "got:", actual2,
              "input:", test_case2)
    else:
        print("Test 2 passed")


if __name__ == '__main__':
    test_find_smallest()
