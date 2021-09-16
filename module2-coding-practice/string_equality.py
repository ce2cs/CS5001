"""
Write a program that reads in a word from the keyboard and prints
"Hi, how are you" and "Done" if someone enters the word "Hi" (capitalization matters).
Otherwise it just prints "Done". For example,

Hi
Hi, how are you?
Done

Bye
Done
"""


def main():
    greeting = input()
    if greeting == "Hi":
        print("Hi, how are you?")
    print("Done")


if __name__ == '__main__':
    main()
