from itertools import count


def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    buses = []
    for bus in input_data[1].split(","):
        try:
            buses.append(int(bus))
        except:
            buses.append(bus)

    return int(input_data[0]), buses


if __name__ == '__main__':
    n, input = load_data()
    buses = tuple((i, b) for i, b in enumerate(input) if isinstance(b, int))
    step = 1
    for i, b in buses:
        n = next(c for c in count(n, step) if (c + i) % int(b) == 0)
        step *= int(b)
    print(n)
