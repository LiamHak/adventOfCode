def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()

    numbers = []
    for line in input_data:
        numbers.append(int(line))

    return numbers


def is_sum(index, list):
    for i in range(index - 25, index):
        for j in range(i, index):
            if list[i] + list[j] == list[index]:
                return True
    return False


if __name__ == '__main__':
    numbers = load_data()
    for i in range(25, len(numbers)):
        if not is_sum(i, numbers):
            print(numbers[i])
            break

