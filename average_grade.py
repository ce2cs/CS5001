import random


def average_grade(grades):
    """
    Return the average grade of input grades list
    :param grades: list of integers
    :return: float, the average of grades
    """
    i = 0
    # calculate the sum of grades
    sum_grade = 0
    while i < len(grades):
        sum_grade += grades[i]
        i += 1
    # the average grade is sum of grades divide by number of grades
    return sum_grade / len(grades)


def main():
    """
    Test function of average_grade
    :return: None
    """
    i = 0
    test_grades = []
    # generate 10 random grades
    while i < 10:
        test_grades.append(random.random() * 100)
        i += 1
    actual_average_grade = average_grade(test_grades)
    # use built-in functions
    expected_average_grade = sum(test_grades) / len(test_grades)
    if actual_average_grade == expected_average_grade:
        print("Test Passed!")
    else:
        print("Test Failed!\nInputs are:")
        print(test_grades)


if __name__ == '__main__':
    main()
