import math


def float_is_equal(n1, n2, threshold):
    return math.fabs(n1 - n2) <= threshold


def main():
    test_paras = [
        (1000., 1000.001, 1e-3),
        (1000., 1000.002, 1e-3),
        (1e-15, 1e-10, 1e-10),
        (1e-15, 1e-10, 1e-15)
    ]

    expected = [
        True,
        False,
        True,
        False,
    ]

    for i in range(len(test_paras)):
        pass_or_fail = "passed" if expected[i] == float_is_equal(*test_paras[i]) else "failed"
        print(pass_or_fail, "Test Case", i, "parameters:", test_paras[i], "expected:", expected[i])


if __name__ == '__main__':
    main()
