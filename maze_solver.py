import sys


class MazeSolver:
    def __init__(self):
        """
        Initializer of the maze solver
        """
        self.maze = None
        self.direction = None
        self.distance = None
        self.path = None

    def run(self):
        """
        Entry of the maze game
        :return: None
        """
        while True:
            try:
                command_idx = self.get_command()
                if command_idx == 1:
                    self.read_maze_from_keyboard()
                if command_idx == 2:
                    self.read_maze_from_file()
                if command_idx == 3:
                    # if user input find exit before input file, raise error
                    if self.maze is None:
                        raise ValueError("Please input the maze from "
                                         "keyboard or file first\n")
                    self.find_exit()
                if command_idx == 4:
                    self.print_maze()
                if command_idx == 5:
                    # quit the game
                    print("You quit the game")
                    return

            except Exception as e:
                # catch all possible error
                print(e)
                print("please try again\n")

    def read_maze_from_keyboard(self):
        """
        read maze from keyboard and store it to a 2d list
        :return: None
        """
        try:
            width, height = input(
                "Please input the width and height of "
                "the maze (separated by a space): "
            ).split(" ")
            width = int(width)
            height = int(height)
        except Exception as e:
            raise ValueError("Please input the width and height "
                             "of the maze (separated by a space)")

        maze = []
        print("Please input the maze, X presents wall, "
              "space presents open space, E presents exit, "
              "the exit should only occur on the perimeter in the maze, "
              "each line is the one row of the maze")
        for _ in range(height):
            maze.append([])
            line = input()
            for letter in line:
                maze[-1].append(letter)
        # check if the maze is valid
        self.check_maze(maze, width, height)
        # because we changed the maze, current direction, path will no longer
        # be valid, so we need to clear cache before store the maze
        self._clear_cached()
        self.maze = maze

    def read_maze_from_file(self):
        """
        read maze from a file and store it to a 2d list
        :return: None
        """
        filename = input("please input the file name: ")
        try:
            with open(filename) as f:
                # need to strip the last "\n"
                width, height = f.readline().strip().split(" ")
                width = int(width)
                height = int(height)
                maze = []
                for _ in range(height):
                    maze.append([])
                    for letter in f.readline().strip():
                        maze[-1].append(letter)
                self.check_maze(maze, width, height)
                self._clear_cached()
                self.maze = maze
        except FileNotFoundError as e:
            raise FileExistsError("Input file does not exist")

    def find_exit(self):
        """
        Use BFS algorithm to find a path, if there is a path to exit,
        it will print the shortest path to the nearest exit,
        if it does not have a reachable exit,
        it will raise a error
        :return: None
        """
        # check if the maze is inputted
        if self.maze is None:
            raise ValueError("You should input maze first!")

        height = len(self.maze)
        width = len(self.maze[0])

        start_row, start_col = input(
            "Please input row number and start col number,"
            "separated by a space: "
        ).split(" ")

        start_row = int(start_row)
        start_col = int(start_col)
        # check the validation of start point
        if start_row >= height or start_row < 0 or \
                start_col >= width or start_col < 0:
            raise ValueError(
                "Please input valid integer of the start row and col number, "
                "The start_row should be bounded in the maze"
            )

        if self.maze[start_row][start_col] == "X":
            raise ValueError("Input position is occupied by a wall!")

        # initialize the path, distance, direction
        self.path = None
        self.distance = [[sys.maxsize for _ in range(width)] for _ in range(height)]
        self.direction = [[None for _ in range(width)] for _ in range(height)]

        # distance to start point is 0
        self.distance[start_row][start_col] = 0

        # BFS queue
        work_list = [(start_row, start_col)]

        # all possible moves
        moves = {
            'N': (-1, 0),
            'S': (1, 0),
            'W': (0, -1),
            'E': (0, 1)
        }

        # do BFS search
        while len(work_list) > 0:
            curr_row, curr_col = work_list.pop(0)
            for direct in moves:
                neighbor_row = curr_row + moves[direct][0]
                neighbor_col = curr_col + moves[direct][1]

                # check if the neighbor outside the maze
                if neighbor_row < 0 or neighbor_row >= height or \
                        neighbor_col < 0 or neighbor_col >= width:
                    continue
                # check if the neighbor is a wall
                if self.maze[neighbor_row][neighbor_col] == 'X':
                    continue
                # check if the neighbor is visited
                if self.distance[neighbor_row][neighbor_col] != sys.maxsize:
                    continue

                # store the direction and distance of neighbor position
                self.direction[neighbor_row][neighbor_col] = direct
                self.distance[neighbor_row][neighbor_col] = \
                    self.distance[curr_row][curr_col] + 1

                # append neighbor node to the end of the queue
                work_list.append((neighbor_row, neighbor_col))

        # find the nearest exit point
        exit_row = -1
        exit_col = -1
        nearest_distance = sys.maxsize

        for row in range(height):
            for col in range(width):
                if self.maze[row][col] == 'E':
                    if self.distance[row][col] < nearest_distance:
                        exit_row, exit_col = row, col
                        nearest_distance = self.distance[row][col]

        # if no exit point can be reached, raise error
        if nearest_distance == sys.maxsize:
            raise ValueError("Cannot find a exit")

        # generate path and print it
        self.get_path_to_exit(start_row, start_col, exit_row, exit_col)
        self._print_maze(self.path)

    def get_path_to_exit(self, start_row, start_col, exit_row, exit_col):
        """
        get shortest path from start point to exit point
        :param start_row: Integer
        :param start_col: Integer
        :param exit_row: Integer
        :param exit_col: Integer
        :return: None
        """
        height = len(self.maze)
        width = len(self.maze[0])
        # initialize the path by a deep copy of maze

        self.path = [
            [
                self.maze[row][col] for col in range(width)
            ]
            for row in range(height)
        ]

        self.path[start_row][start_col] = 'S'

        # start from exit point
        current_row = exit_row
        current_col = exit_col

        # reverse the move process
        reverse_moves = {
            'N': (1, 0),
            'S': (-1, 0),
            'W': (0, 1),
            'E': (0, -1)
        }

        # draw the path follow the direction
        while True:
            next_row = current_row + reverse_moves[self.direction[current_row][current_col]][0]
            next_col = current_col + reverse_moves[self.direction[current_row][current_col]][1]
            # when move to the start point, return
            if next_row == start_row and next_col == start_col:
                break
            self.path[next_row][next_col] = '*'
            current_row = next_row
            current_col = next_col

    def print_maze(self):
        """
        print the maze, if user already called find exit, it will
        print the path
        :return: None
        """
        if self.path:
            self._print_maze(self.path)
        else:
            self._print_maze(self.maze)

    @staticmethod
    def _print_maze(maze):
        """
        print 2d maze
        :param maze: 2d list
        :return: None
        """
        for row in range(len(maze)):
            line = ""
            for col in range(len(maze[0])):
                line += maze[row][col]
            print(line)

    @staticmethod
    def get_command():
        """
        get command from User
        :return: None
        """
        command_idx = input("Please input your command, you can select from\n"
                            "1. read maze from keyboard\n"
                            "2. read maze from file\n"
                            "3. find exit\n"
                            "4. print maze\n"
                            "5. quit game\n"
                            "Please your command by its index: ")
        try:
            command_idx = int(command_idx)
            if command_idx > 5 or command_idx <= 0:
                raise ValueError("Please input a number within 1 to 5\n")
            return command_idx
        except Exception as e:
            raise ValueError("Please input a integer within 1 to 5\n")

    @staticmethod
    def check_maze(maze, width, height):
        """
        check the if the 2d maze is valid
        :param maze: 2d list
        :param width: desired width
        :param height: desired height
        :return: None
        """
        if len(maze) != height:
            raise ValueError(
                "You should input maze lines that equal to height"
            )
        for row in range(height):
            if len(maze[row]) != width:
                raise ValueError(
                    "You should input the maze line that equal to width"
                )
            for col in range(width):
                if maze[row][col] not in [" ", "X", "E"]:
                    raise ValueError(
                        "Your maze should only contains space, X and E"
                    )
                if maze[row][col] == "E" and row != 0 and col != 0 and \
                        col != width - 1 and row != height - 1:
                    raise ValueError(
                        "Exit can only appear on the perimeter of the maze"
                    )

    def _clear_cached(self):
        """
        clear the cached maze, direction, distance and path
        :return: None
        """
        self.maze = None
        self.direction = None
        self.distance = None
        self.path = None


if __name__ == '__main__':
    ms = MazeSolver()
    ms.run()
