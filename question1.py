def insertion_sort(input_list):
    """
    sort the input_list by increase order using insertion sort algorithm
    :param input_list: list of comparable items
    :return: sorted list
    """
    new_list = []
    # pick up a item
    for item in input_list:
        # insert first item directly
        if len(new_list) == 0:
            new_list.append(item)
        else:
            index = 0
            # insert the picked item before the
            # first prior item that is lower and equal to itself
            while index < len(new_list):
                if item <= new_list[index]:
                    break
                index += 1
            new_list.insert(index, item)
    return new_list
