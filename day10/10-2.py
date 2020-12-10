def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    numbers = []
    for line in input_data:
        numbers.append(int(line))

    return numbers


if __name__ == '__main__':
    numbers = load_data()
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()

    arrangements = [1] + [0]*numbers[-1]
    for i in numbers[1:]:
        arrangements[i] = arrangements[i-3] + arrangements[i-2] + arrangements[i-1]

    print(arrangements[-1])
