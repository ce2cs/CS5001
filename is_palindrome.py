def is_palindrome(word):
    i = 0
    while i < len(word) // 2:
        if word[i] != word[len(word) - i - 1]:
            return False
        i += 1
    return True


def main():
    test_words = ["abba", "bbaa", "a", "122", "aba", "abc"]
    expected = [True, False, True, False, True, False]
    i = 0
    passed = True
    while i < len(test_words):
        if is_palindrome(test_words[i]) != expected[i]:
            passed = False
            print("Test Failed! Input word is:", test_words[i])
        i += 1
    if passed:
        print("Test Passed!")


if __name__ == '__main__':
    main()
