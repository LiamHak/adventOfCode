import time


def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()

    numbers = []
    for line in input_data:
        numbers.append(int(line))

    return numbers


def is_sum(index, list):
    preamble_set = set(list[index - 25: index])
    for i in range(index - 25, index):
        if list[index] - list[i] in preamble_set:
            return True
    return False


if __name__ == '__main__':

    numbers = load_data()

    t0 = time.time()
    for i in range(25, len(numbers)):
        if not is_sum(i, numbers):
            print(numbers[i])
            break
    t1 = time.time()
    print("Runtime: ", t1 - t0)
