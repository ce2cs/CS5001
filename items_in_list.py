def items_in_list(list1, list2):
    result = []
    for ele1 in list1:
        if ele1 in list2 and ele1 not in result:
            result.append(ele1)
    return result


def main():
    list1 = [3, 5, 1, 23, 2]
    list2 = [12, 23, 1, 1, 2, 5]
    expected1 = [5, 1, 23, 2]
    actual1 = items_in_list(list1, list2)
    list3 = [3, 5, 1, 23, 2]
    list4 = [12, 23, 5]
    expected2 = [5, 23]
    actual2 = items_in_list(list3, list4)
    if actual1 == expected1:
        print("Test 1 Passed!")
    else:
        print("Test 1 Failed!\nInputs are:")
        print(list1)
        print(list2)

    if actual2 == expected2:
        print("Test 2 Passed!")
    else:
        print("Test 2 Failed!\nInputs are:")
        print(list3)
        print(list4)


if __name__ == '__main__':
    main()
