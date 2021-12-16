'''
Write a recursive version of list_of_strings_loop
Write a useful comment for your function
'''
import random
import unittest


def list_of_strings_recursion(number_of_strings):
    """
    generate list of random alphabetic strings recursively,
    the length of list will equal to number_of_strings
    :param number_of_strings: Integer
    :return: random strings list
    """
    if number_of_strings == 0:
        return []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_of_strings = []
    string_length = random.randint(1, 5)
    this_word = ""
    for character in range(string_length):
        this_word += random.choice(alphabet)
    # every time add generated random word to return list
    list_of_strings.append(this_word)
    # recursively call this function with input - 1
    # add append the returned list to current return list
    list_of_strings.extend(list_of_strings_recursion(number_of_strings - 1))
    return list_of_strings


def list_of_strings_loop(number_of_strings):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_of_strings = []
    for word in range(number_of_strings):
        string_length = random.randint(1, 5)
        this_word = ""
        for character in range(string_length):
            this_word += random.choice(alphabet)
        list_of_strings.append(this_word)
    return list_of_strings


if __name__ == '__main__':
    # test the function list_of_strings_recursion
    tc = unittest.TestCase()
    # use random seed to control the generated random string
    random.seed(0)
    actual = list_of_strings_loop(10)
    # remember to reset the random seed every time call
    random.seed(0)
    expected = list_of_strings_recursion(10)
    tc.assertEqual(actual, expected)
