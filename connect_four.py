class ConnectFour:
    def __init__(self):
        self._row_num = 6
        self._col_num = 7
        self._board = [[' ' for _ in range(self._col_num)] for _ in range(self._row_num)]
        self._game_over = False
        self._moves_stack = []
        self._winner = None
        self._is_column_full = [False] * self._col_num
        self._full_column_number = 0

    def add_piece(self, column):
        if column >= self._col_num or column < 0:
            raise ValueError("input column is outside of the board")
        if self.is_game_over():
            raise ValueError("game is already over")
        if self._is_column_full[column]:
            raise ValueError("column is already full")

        curr_player = self.get_current_player()
        for row in reversed(range(self._row_num)):
            if self._board[row][column] == ' ':
                self._board[row][column] = curr_player
                self._moves_stack.append((curr_player, row, column))
                max_length = self._get_connected_length(row, column)
                if max_length >= 4:
                    self._game_over = True
                    self._winner = curr_player
                if row == 0:
                    self._is_column_full[column] = True
                    self._full_column_number += 1
                    if self._full_column_number == self._col_num:
                        self._game_over = True
                break

    def get_winner(self):
        return self._winner

    def undo(self):
        if len(self._moves_stack) == 0:
            return

        player, row, col = self._moves_stack.pop()
        if row == 0:
            if self._full_column_number == self._col_num:
                self._game_over = False
            self._full_column_number -= 1
            self._is_column_full[col] = False

        max_length = self._get_connected_length(row, col)
        if max_length >= 4:
            self._game_over = False
            self._winner = None

        self._board[row][col] = ' '

    def is_game_over(self):
        return self._game_over

    def get_current_player(self):
        curr_player = 'X'
        if len(self._moves_stack) > 0 and self._moves_stack[-1][0] == 'X':
            curr_player = 'O'
        return curr_player

    def __str__(self):
        horizontal_line = '-' * (self._col_num * 2 + 1)
        board_str = ''
        for row in range(self._row_num):
            board_str += '|' + '|'.join(self._board[row]) + '|' + '\n'
            board_str += horizontal_line + '\n'
        board_str = board_str[:-1]
        return board_str

    def _get_connected_length(self, central_row, central_col):
        player = self._board[central_row][central_col]
        directions = [
            ((0, 1), (0, -1)),
            ((1, 0), (-1, 0)),
            ((1, 1), (-1, -1)),
            ((1, -1), (-1, 1)),
        ]

        connected_length = 0
        for direction in directions:
            direction_length = 1
            for row_move, col_move in direction:
                row_ptr = central_row + row_move
                col_ptr = central_col + col_move
                while 0 <= row_ptr < self._row_num and 0 <= col_ptr < self._col_num:
                    if self._board[row_ptr][col_ptr] != player:
                        break
                    direction_length += 1
                    row_ptr += row_move
                    col_ptr += col_move
            connected_length = max(direction_length, connected_length)
        return connected_length
