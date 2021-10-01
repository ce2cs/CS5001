def translate(english_day):
    """
    translate a English day word into French
    :param english_day: string, English day word,
    both lowercase and uppercase should be allowed
    :return: string, the French translation
    """
    french_dictionary = {
        "monday": "lundi",
        "tuesday": "mardi",
        "wednesday": "mercredi",
        "thursday": "jeudi",
        "friday": "vendredi",
        "saturday": "samedi",
        "sunday": "dimanche",
    }

    if english_day.lower() not in french_dictionary:
        return "wrong input"
    return french_dictionary[english_day.lower()]


def main():
    """
    test program for french_dictionary
    :return: None
    """
    test_paras = [
        ("MONDAY",),
        ("Tuesday",),
        ("Sleepday",)
    ]

    expected = [
        "Lundi",
        "Mardi",
        "wrong input"
    ]

    for i in range(len(test_paras)):
        pass_or_fail = "passed" \
            if expected[i] == translate(*test_paras[i]) else "failed"
        print(pass_or_fail, "Test Case", i, "parameters:",
              test_paras[i], "expected:", expected[i])


if __name__ == '__main__':
    main()
