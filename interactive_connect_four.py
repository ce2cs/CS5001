from connect_four import ConnectFour


def main():
    cf = ConnectFour()
    print(cf)
    while not cf.is_game_over():
        print("Current player:", cf.get_current_player())
        try:
            column = int(input("Please place a piece: "))
            cf.add_piece(column)
            print(cf)
        except TypeError:
            print("Please input a integer")
        except Exception as e:
            print(e)

    if cf.is_game_over():
        print("Game Over")
        print("Winner is", cf.get_winner())


if __name__ == '__main__':
    main()
