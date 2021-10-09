import random


def average_grade(grades):
    i = 0
    sum_grade = 0
    while i < len(grades):
        sum_grade += grades[i]
        i += 1
    return sum_grade / len(grades)


def main():
    i = 0
    test_grades = []
    while i < 10:
        test_grades.append(random.random() * 100)
        i += 1
    actual_average_grade = average_grade(test_grades)
    expected_average_grade = sum(test_grades) / len(test_grades)
    if actual_average_grade == expected_average_grade:
        print("Test Passed!")
    else:
        print("Test Failed!\nInputs are:")
        print(test_grades)


if __name__ == '__main__':
    main()
