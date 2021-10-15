def add_evens(lst):
    result = 0
    for num in lst:
        if num % 2 == 0:
            result += num
    return result


def main():
    source = [3, 5, 1, 23, 55, 2]
    expected = 2
    actual = add_evens(source)
    if actual == expected:
        print("Test Passed!")
    else:
        print("Test Failed!\nInputs are:")
        print(source)


if __name__ == '__main__':
    main()
