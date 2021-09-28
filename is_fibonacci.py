def is_fibonacci(n):
    i = 0
    j = 1
    while j < n:
        tmp = j
        j += i
        i = tmp
    return j == n


def main():
    test_paras = [
        (1,),
        (2,),
        (7,),
        (8,),
        (88,),
        (89,),
        (90,)
    ]

    expected = [
        True,
        True,
        False,
        True,
        False,
        True,
        False
    ]

    for i in range(len(test_paras)):
        pass_or_fail = "passed" if expected[i] == is_fibonacci(*test_paras[i]) else "failed"
        print(pass_or_fail, "Test Case", i, "parameters:", test_paras[i], "expected:", expected[i])


if __name__ == '__main__':
    main()
