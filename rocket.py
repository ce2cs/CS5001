def rocket():
    """
    print rocket with input size
    :return: None
    """
    rocket_size = int(input())
    if rocket_size < 3:
        print("Rocket sizes must be at least 3")
        return

    # cal width of the rocket
    width = rocket_size * 4 + 2
    print_head(width)
    print_divider(width)
    print_down_triangle_compartment(width)
    print_upper_triangle_compartment(width)
    print_divider(width)
    print_upper_triangle_compartment(width)
    print_down_triangle_compartment(width)
    print_divider(width)
    print_down_triangle_compartment(width)
    print_upper_triangle_compartment(width)
    print_divider(width)
    print_head(width)


def print_head(width):
    """
    print rocket head
    :param width: the width of the rocket
    :return: None
    """
    # cal slash and space number in a line
    slash_number = 1
    space_number = width // 2 - 2
    while slash_number < width // 2 - 1:
        print(' ' * space_number +
              "/" * slash_number +
              "**" +
              "\\" * slash_number +
              ' ' * space_number)
        slash_number += 1
        space_number -= 1


def print_divider(width):
    """
    print rocket divider between compartments
    :param width: the width of the rocket
    :return: None
    """
    print('+' + '=*' * (width // 2 - 1) + '+')


def print_upper_triangle_compartment(width):
    """
    print rocket compartments within upward triangles
    :param width: the width of the rocket
    :return: None
    """
    # triangle_numbers '/\' of left half compartment
    # equal to the value of rocket size
    triangle_number = (width // 2 - 1) // 2
    # cal dot number between '|' and first triangle
    dot_num = 0
    while triangle_number > 0:
        print('|' +
              '.' * dot_num +
              '\\/' * triangle_number +
              '.' * dot_num * 2 +
              '\\/' * triangle_number +
              '.' * dot_num +
              '|')
        dot_num += 1
        triangle_number -= 1


def print_down_triangle_compartment(width):
    """
    print rocket compartments within downward triangles
    :param width: the width of the rocket
    :return: None
    """
    triangle_number = 1
    # cal dot number between '|' and first triangle
    dot_num = (width // 2 - 1 - triangle_number * 2) // 2
    while dot_num >= 0:
        print('|' +
              '.' * dot_num +
              '/\\' * triangle_number +
              '.' * dot_num * 2 +
              '/\\' * triangle_number +
              '.' * dot_num +
              '|')
        dot_num -= 1
        triangle_number += 1


if __name__ == '__main__':
    rocket()
