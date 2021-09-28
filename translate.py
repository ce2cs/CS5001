def translate(english_day):
    french_dictionary = {
        "monday": "Lundi",
        "tuesday": "Mardi",
        "wednesday": "Mercredi",
        "thursday": "Jeudi",
        "friday": "Vendredi",
        "saturday": "Samedi",
        "sunday": "Dimanche",
    }

    if english_day.lower() not in french_dictionary:
        return "wrong input"
    return french_dictionary[english_day.lower()]


def main():
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
