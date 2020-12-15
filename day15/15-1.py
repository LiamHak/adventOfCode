

if __name__ == '__main__':
    starting_numbers = [2, 0, 1, 9, 5, 19]
    numbers_spoken = starting_numbers.copy()
    numbers_spoken.reverse()

    while len(numbers_spoken) < 2020:
        last_spoken = numbers_spoken[0]
        dist = next((i + 1 for i, num in enumerate(numbers_spoken[1:]) if num == last_spoken), 0)
        numbers_spoken = [dist] + numbers_spoken

    print(numbers_spoken[0])