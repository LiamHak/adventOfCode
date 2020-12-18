from queue import Queue


def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    eq_queues = []
    for line in input_data:
        queue = Queue()
        for char in line.strip():
            if char != " ":
                queue.put(char)
        eq_queues.append(queue)

    return eq_queues


def solve_eq(eq):
    eq_result = 0
    next_op = "+"
    while not eq.empty():
        char = eq.get()
        if char == "(":
            open_brackets = 1
            sub_eq = Queue()
            while open_brackets > 0:
                char = eq.get()
                if char == "(":
                    open_brackets += 1
                elif char == ")":
                    open_brackets -= 1
                sub_eq.put(char)
            if next_op == "+":
                eq_result += solve_eq(sub_eq)
            elif next_op == "*":
                eq_result = eq_result * solve_eq(sub_eq)
        elif char == ")":
            continue
        elif char == "+" or char == "*":
            next_op = char
        else:
            if next_op == "+":
                eq_result += int(char)
            elif next_op == "*":
                eq_result = eq_result * int(char)

    return eq_result


if __name__ == '__main__':
    equations = load_data()
    results = []
    for eq in equations:
        results.append(solve_eq(eq))
    print(sum(results))