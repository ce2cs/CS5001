'''
Write a recursive version of list_of_strings_loop
Write a useful comment for your function
'''
import random


def list_of_strings_loop(number_of_strings):
    if number_of_strings == 0:
        return []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_of_strings = []
    string_length = random.randint(1, 5)
    this_word = ""
    for character in range(string_length):
        this_word += random.choice(alphabet)
    list_of_strings.append(this_word)
    list_of_strings.extend(list_of_strings_loop(number_of_strings - 1))
    return list_of_strings


if __name__ == '__main__':
    print(list_of_strings_loop(10))
