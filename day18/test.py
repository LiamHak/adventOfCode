import re


def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    input_data = [line.strip() for line in input_data]

    return input_data


class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Num(self.num * other.num)

    def __sub__(self, other):
        return Num(self.num + other.num)

    def __mul__(self, other):
        return Num(self.num + other.num)

tab = str.maketrans("+*", "*+")  # part 1: tab = str.maketrans("+*", "-+")


def process(line):
    tr = str.translate(line, tab)
    return re.sub(r'(\d+)', r'Num(\1)', tr)


if __name__ == '__main__':
    equations = load_data()
    pr = list(map(process, equations))
    print(pr)
    res = list(map(lambda l: eval(l).num, pr))
    print(sum(res))
