import random


def flowchart_function(input_list):
    """
    Input a any kinds of list that every elements
    can be converted to string, return a lines of string as output,
    each element at a new line. Each line of the output is:
    repeat element for line number (start for 1) times
    :param input_list: list of Objects that can be converted to string
    :return: output string
    """
    output_string = ""
    # element idx counter
    n = 0
    while n < len(input_list):
        # repeat n + 1 times
        for _ in range(n + 1):
            output_string += str(input_list[n])
        output_string += "\n"
        n += 1
    return output_string


def test_flowchart_function():
    """
    Test function for flowchart_function
    :return: None
    """
    test_case1 = ["a", "b", "c", "d", "e"]
    test_case2 = [1, 2, 3, 4, 5]
    test_case3 = [1.1, 2.2, 3.3]
    test_case4 = [random.random() * 100] * 50
    test_case5 = [(random.random() - 0.5) * 100] * 50
    expected1 = "a\nbb\nccc\ndddd\neeeee\n"
    expected2 = "1\n22\n333\n4444\n55555\n"
    expected3 = "1.1\n2.22.2\n3.33.33.3\n"
    expected4 = '\n'.join([str(test_case4[i]) * (i + 1)
                           for i in range(len(test_case4))]) + '\n'
    expected5 = '\n'.join([str(test_case5[i]) * (i + 1)
                           for i in range(len(test_case5))]) + '\n'
    actual1 = flowchart_function(test_case1)
    if actual1 != expected1:
        print("Test 1 failed, expected:", expected1,
              "got:", actual1,
              "input:", test_case1)
    else:
        print("Test 1 passed")

    actual2 = flowchart_function(test_case2)
    if actual2 != expected2:
        print("Test 2 failed, expected:", expected2,
              "got:", actual2,
              "input:", test_case2)
    else:
        print("Test 2 passed")

    actual3 = flowchart_function(test_case3)
    if actual3 != expected3:
        print("Test 3 failed, expected:", expected3,
              "got:", actual3,
              "input:", test_case3)
    else:
        print("Test 3 passed")

    actual4 = flowchart_function(test_case4)
    if actual4 != expected4:
        print("Test 4 failed, expected:", expected4,
              "got:", actual4,
              "input:", test_case4)
    else:
        print("Test 4 passed")

    actual5 = flowchart_function(test_case5)
    if actual5 != expected5:
        print("Test 5 failed, expected:", expected5,
              "got:", actual5,
              "input:", test_case5)
    else:
        print("Test 5 passed")


if __name__ == '__main__':
    test_flowchart_function()
