class Word:
    def __init__(self, input_word):
        """
        constructor
        :param input_word: string
        """
        # check input format
        if type(input_word) != str:
            print("you must input a string")
        self.input_word = input_word

    def is_palindrome(self, number_of_times):
        """
        check if the input word is palindrome by using
        a stack and a queue
        :param number_of_times: int
        :return: boolean
        """
        # check input parameter
        if type(int) != int or number_of_times <= 0:
            print("you must input a positive integer")

        # use stack and queue to store input word
        stack = Stack()
        queue = Queue()
        for letter in self.input_word:
            stack.push(letter)
            queue.enqueue(letter)

        # every time we check if our current word is a palindrome
        # by dump half of the stack and queue, and check whether
        # dumped result are same.
        for times in range(1, number_of_times + 1):
            # stack and queue are empty means the palindrome time
            # is beyond the real palindrome time
            if stack.is_empty() or queue.is_empty():
                return False
            half_size = len(self.input_word) // (2 * times)
            for _ in range(half_size):
                if stack.pop() != queue.dequeue():
                    return False
        return True

    def is_repeat(self, number_of_repeats):
        """
        use a queue to check if the input word is formed
        by repeat a input times.
        :param number_of_repeats: int
        :return: boolean
        """

        # check input parameter
        if type(number_of_repeats) != int:
            print("you must input a integer")
        if number_of_repeats < 2:
            print("you must input a integer greater or equal to 2")

        # if input word can not be divide by number_of_repeats,
        # then it cannot be formed by a pattern repeat number_of_repeats time
        if len(self.input_word) % number_of_repeats != 0:
            return False

        # use a queue to store the word
        queue = Queue()
        for letter in self.input_word:
            queue.enqueue(letter)

        # get possible repeat pattern
        repeat_pattern_length = len(self.input_word) // number_of_repeats
        repeat_pattern = self.input_word[:repeat_pattern_length]

        # check every letter
        for i in range(repeat_pattern_length):
            if repeat_pattern[i] != queue.dequeue():
                return False
        return True


class Queue:
    def __init__(self):
        """ Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our queue
        """
        self.data = list()

    def enqueue(self, item):
        """ enqueue -- adds something to the end of the queue
        Parameters:
           self -- the current object
           item -- the item to add to the queue
        Returns nothing
        """
        self.data.append(item)

    def dequeue(self):
        """ deqeuue -- removes something from the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        """
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0


class Stack:
    def __init__(self):
        """ Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our stack
        """
        self.data = list()

    def push(self, item):
        """ push -- adds something to the top of the stack
        Parameters:
           self -- the current object
           item -- the item to add to the stack
        Returns nothing
        """
        self.data.append(item)

    def pop(self):
        """ pop -- removes something from the top of the stack
        Parameters:
           self -- the current object
        Returns the top element after removing it from the stack
        """
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0
