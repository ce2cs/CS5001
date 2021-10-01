def chessboard(width, height):
    """
    generate chessboard according to width and height
    :param width: int, the width of the chessboard
    :param height: int, the height of the chessboard
    :return: string, chessboard looks like:
        "BWBWBWBW
         WBWBWBWB
         BWBWBWBW
         WBWBWBWB"
    """
    board = ""
    for h in range(height):
        for w in range(width):
            board += "B" if (h + w) % 2 == 0 else "W"
        board += "\n"
    return board


def main():
    """
    test program for chessboard function
    :return: None
    """
    test_paras = [
        (8, 4),
        (7, 3)
    ]

    expected = [
        "BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\n",
        "BWBWBWB\nWBWBWBW\nBWBWBWB\n"
    ]

    for i in range(len(test_paras)):
        pass_or_fail = "passed" \
            if expected[i] == chessboard(*test_paras[i]) else "failed"
        print(pass_or_fail, "Test Case", i, "parameters:",
              test_paras[i], "expected:", expected[i])


if __name__ == '__main__':
    main()
