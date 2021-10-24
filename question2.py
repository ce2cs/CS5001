def find_median(input_list):
    '''
    find_median takes a list of numbers as input
    and finds the median value in the list. The median value
    is defined as the value for which half the items are larger
    and half the items are smaller.
    For a list of length 5, this means 2 values are larger
    and 2 values are larger.
    So for an odd length list there are an equal number of bigger items, and
    and equal number of smaller items
    For a list of length 6, there are 2 values larger, and two values smaller.
    But this leaves two middle values. In this case we take the
    average of the two:
    (middle1 + middle2) / 2
    So for an even length list, there are equal number smaller and larger,
    but then we always
    have two values left, and must take their average (mean).

    :param input_list: A list of numbers
    :return: The median value of the list
    '''
    size = len(input_list)
    # sorted is a built-in function that will return a sorted list
    sorted_list = sorted(input_list)
    median = 0
    if size % 2 != 0:
        median = sorted_list[size // 2]
    else:
        median = 0.5 * (sorted_list[size // 2 - 1] + sorted_list[(size // 2)])
    return median


def main():
    my_list = list(range(0, 6))
    expected = 2.5
    actual = find_median(my_list)
    if actual != expected:
        print("FAILED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)

    my_list = list(range(0, 5))
    expected = 2
    actual = find_median(my_list)
    if actual != expected:
        print("FAILED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)


if __name__ == "__main__":
    main()
