class ConnectFour:
    """
    The main class of connect four game
    """

    def __init__(self):
        """
        Constructor
        """
        # board size
        self._row_num = 6
        self._col_num = 7
        self.board = [[' ' for _ in range(self._col_num)]
                      for _ in range(self._row_num)]
        # indicate game status
        self._game_over = False
        # a stack that stores all moves
        # each move is represented as follow format:
        # (player, column, row)
        self._moves_stack = []
        # None is undecided or tie, it can also be set as 'X' or 'O'
        self._winner = None
        # indicate whether designated column is full
        self._is_column_full = [False] * self._col_num
        # the number of full column number
        # if all column become full, game is over
        self._full_column_number = 0

    def add_piece(self, column):
        """
        add a piece to the lowest row to designated column
        :param column: Integer
        :return: None
        """
        # handle exceptions
        if column >= self._col_num or column < 0:
            raise ValueError("input column is outside of the board")
        if self.is_game_over():
            raise ValueError("game is already over")
        if self._is_column_full[column]:
            raise ValueError("column is already full")

        # get current player
        curr_player = self.get_current_player()

        # get first empty lowest row
        for row in reversed(range(self._row_num)):
            if self.board[row][column] == ' ':
                self.board[row][column] = curr_player
                # store the move to stack
                self._moves_stack.append((curr_player, row, column))
                # get connected length centred by new piece
                max_length = self._get_connected_length(row, column)
                # if wins, gave over
                if max_length >= 4:
                    self._game_over = True
                    self._winner = curr_player
                # if current column becomes full after place
                # the piece, mark it as full
                if row == 0:
                    self._is_column_full[column] = True
                    self._full_column_number += 1
                    # if all column are full, game over
                    if self._full_column_number == self._col_num:
                        self._game_over = True
                break

    def get_winner(self):
        """
        get the winner of the game
        :return: None, 'X' or 'O'
        """
        return self._winner

    def undo(self):
        """
        undo a move
        :return: None
        """
        if len(self._moves_stack) == 0:
            raise ValueError("There is no move stored")

        # remove the latest move
        player, row, col = self._moves_stack.pop()
        # if the removed piece is the last piece that
        # can be put onto a column, mark the column as not full
        if row == 0:
            # if all columns are originally full, activate the game
            if self._full_column_number == self._col_num:
                self._game_over = False
            self._full_column_number -= 1
            self._is_column_full[col] = False

        # if the latest move decides the winner, reset the winner to None
        max_length = self._get_connected_length(row, col)
        if max_length >= 4:
            self._game_over = False
            self._winner = None

        self.board[row][col] = ' '

    def is_game_over(self):
        """
        Get the game status
        :return: boolean
        """
        return self._game_over

    def get_current_player(self):
        """
        Get player who takes next move, initially is 'X'
        :return: String, alternatively 'X' or 'O'
        """
        curr_player = 'X'
        if len(self._moves_stack) > 0 and self._moves_stack[-1][0] == 'X':
            curr_player = 'O'
        return curr_player

    def __str__(self):
        """
        Serialize the board
        :return: String
        """
        horizontal_line = '-' * (self._col_num * 2 + 1)
        board_str = ''
        for row in range(self._row_num):
            board_str += '|' + '|'.join(self.board[row]) + '|' + '\n'
            board_str += horizontal_line + '\n'
        return board_str

    def _get_connected_length(self, central_row, central_col):
        """
        Helper function to get maximum connected length
        centred by designated piece
        :param central_row: Integer
        :param central_col: Integer
        :return: Integer
        """
        # get current player
        player = self.board[central_row][central_col]
        # all possible connect direction
        directions = [
            ((0, 1), (0, -1)),  # horizontal
            ((1, 0), (-1, 0)),  # vertical
            ((1, 1), (-1, -1)),  # top-left diagonal
            ((1, -1), (-1, 1)),  # top-right diagonal
        ]

        connected_length = 0
        for direction in directions:
            direction_length = 1
            # sum up the connect length by two opposite direction
            for row_move, col_move in direction:
                # indicate the board grid we want to examine
                row_ptr = central_row + row_move
                col_ptr = central_col + col_move
                # while the gird does not place outside the board,
                # extend to current direction by one step
                while 0 <= row_ptr < self._row_num \
                        and 0 <= col_ptr < self._col_num:
                    # if the pieces line was cutoff, break
                    if self.board[row_ptr][col_ptr] != player:
                        break
                    direction_length += 1
                    row_ptr += row_move
                    col_ptr += col_move
            connected_length = max(direction_length, connected_length)
        return connected_length
