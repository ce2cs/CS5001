def rocket(rocket_size):
    """
    print rocket with input size
    :param rocket_size: integer
    :return: None
    """
    if rocket_size < 3:
        print("Rocket sizes must be at least 3")
        return

    # cal width of the rocket
    width = rocket_size * 4 + 2
    return rocket_head(width) + \
           rocket_divider(width) + \
           rocket_upper_triangle_compartment(width) + \
           rocket_down_triangle_compartment(width) + \
           rocket_divider(width) + \
           rocket_down_triangle_compartment(width) + \
           rocket_upper_triangle_compartment(width) + \
           rocket_divider(width) + \
           rocket_upper_triangle_compartment(width) + \
           rocket_down_triangle_compartment(width) + \
           rocket_divider(width) + \
           rocket_head(width)


def rocket_head(width):
    """
    print rocket head
    :param width: the width of the rocket
    :return: None
    """
    # cal slash and space number in a line
    slash_number = 1
    space_number = width // 2 - 2
    lines = ""
    while slash_number < width // 2 - 1:
        lines += ' ' * space_number + \
                 "/" * slash_number + \
                 "**" + \
                 "\\" * slash_number + \
                 ' ' * space_number + \
                 "\n"
        slash_number += 1
        space_number -= 1
    return lines


def rocket_divider(width):
    """
    print rocket divider between compartments
    :param width: the width of the rocket
    :return: None
    """
    return '+' + '=*' * (width // 2 - 1) + '+' + "\n"


def rocket_upper_triangle_compartment(width):
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
    lines = ""
    while triangle_number > 0:
        lines += '|' + \
                 '.' * dot_num + \
                 '\\/' * triangle_number + \
                 '.' * dot_num * 2 + \
                 '\\/' * triangle_number + \
                 '.' * dot_num + \
                 '|' + \
                 "\n"
        dot_num += 1
        triangle_number -= 1
    return lines


def rocket_down_triangle_compartment(width):
    """
    print rocket compartments within downward triangles
    :param width: the width of the rocket
    :return: None
    """
    triangle_number = 1
    # cal dot number between '|' and first triangle
    dot_num = (width // 2 - 1 - triangle_number * 2) // 2
    lines = ""
    while dot_num >= 0:
        lines += '|' + \
                 '.' * dot_num + \
                 '/\\' * triangle_number + \
                 '.' * dot_num * 2 + \
                 '/\\' * triangle_number + \
                 '.' * dot_num + \
                 '|' + \
                 "\n"
        dot_num -= 1
        triangle_number += 1
    return lines


if __name__ == '__main__':
    print(rocket(5))
