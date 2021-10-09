import random


def within_budget(prices, budget):
    filtered_prices = []
    i = 0
    while i < len(prices):
        if prices[i] <= budget:
            filtered_prices.append(prices[i])
        i += 1
    return filtered_prices


def main():
    test_prices = []
    i = 0
    while i < 100:
        test_prices.append(random.randint(0, 100))
        i += 1
    test_budget = random.randint(0, 100)
    actual_filtered_prices = within_budget(test_prices, test_budget)
    expected_filtered_prices = filter(lambda x: x <= test_budget, test_prices)
    while i < 100:
        if actual_filtered_prices[i] != expected_filtered_prices[i]:
            print("Test Failed!\nInputs are:")
            print(test_prices)
            return
    print("Test Passed!")


if __name__ == '__main__':
    main()
