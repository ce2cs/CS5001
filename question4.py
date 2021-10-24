def multiples_of_three(threshold):
    """
    Get all integers that are multiples of three
    less and equal to threshold, note that 0 is also
    a multiple of three
    :param threshold: Integer
    :return: Integer of list contains multiples of 3
    """
    result = []
    # enumerate all possible factor of multiples of 3
    factor = 0
    while factor * 3 <= threshold:
        result.append(factor * 3)
        factor += 1
    return result


def test_multiple_of_three():
    """
    Test function of multiples_of_three
    :return: None
    """
    test_case1 = 5
    test_case2 = 10
    test_case3 = 50
    expected1 = [0, 3]
    expected2 = [0, 3, 6, 9]
    expected3 = [0, 3, 6, 9, 12, 15, 18, 21, 24,
                 27, 30, 33, 36, 39, 42, 45, 48]
    actual1 = multiples_of_three(test_case1)
    if actual1 != expected1:
        print("Test 1 failed, expected:", expected1,
              "got:", actual1,
              "input:", test_case1)
    else:
        print("Test 1 passed")

    actual2 = multiples_of_three(test_case2)
    if actual2 != expected2:
        print("Test 2 failed, expected:", expected2,
              "got:", actual2,
              "input:", test_case2)
    else:
        print("Test 2 passed")

    actual3 = multiples_of_three(test_case3)
    if actual3 != expected3:
        print("Test 3 failed, expected:", expected3,
              "got:", actual3,
              "input:", test_case3)
    else:
        print("Test 3 passed")


if __name__ == '__main__':
    test_multiple_of_three()
