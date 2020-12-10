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
    numbers.sort()
    diffs = []
    diffs.append(numbers[0])
    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i-1])
    diffs.append(3)
    one_jolt_diffs = diffs.count(1)
    three_jolt_diffs = diffs.count(3)
    ans = one_jolt_diffs * three_jolt_diffs
    print(ans)