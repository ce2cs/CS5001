def main():
    rating = int(input("Input rating:"))
    if rating > 100:
        print("Buy a lot")
    elif rating > 76:
        print("Buy a little")
    elif rating >= 50:
        print("Stay")
    elif rating > 25:
        print("Sell")
    else:
        print("Sell! Sell! Sell!")


if __name__ == '__main__':
    main()
