def number_greater_than(list1, list2):
    """
    Return the number of elements in list1 that is
    greater than list2 at same position
    :param list1: Integer of list
    :param list2: Integer of list
    :return: Count of greater elements
    """
    result = 0
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            result += 1
    return result


def main():
    """
    Test function of number_greater_than
    :return: None
    """
    list1 = [3, 5, 1, 23, 55, 2]
    list2 = [12, 23, 1, 1, 2, 5]
    expected = 2
    actual = number_greater_than(list1, list2)
    if actual == expected:
        print("Test Passed!")
    else:
        print("Test Failed!\nInputs are:")
        print(list1)
        print(list2)


if __name__ == '__main__':
    main()
