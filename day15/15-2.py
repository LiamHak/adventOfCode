

if __name__ == '__main__':
    starting_numbers = [2, 0, 1, 9, 5, 19]
    numbers_spoken = dict()
    for i, num in enumerate(starting_numbers[:-1]):
        numbers_spoken[num] = i

    last_spoken = starting_numbers[-1]

    for i in range(len(starting_numbers), 30000000):
        try:
            dist = i - numbers_spoken[last_spoken] - 1
        except:
            dist = 0

        numbers_spoken[last_spoken] = i - 1
        last_spoken = dist

    print(last_spoken)