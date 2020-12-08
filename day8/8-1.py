def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()

    cleaned_data = []

    for line in input_data:
        cleaned_data.append(line.replace("\n", "").split(" "))

    return cleaned_data


def perform_instruction(instruction):
    offset = 1
    acc = 0
    if instruction[0] == "acc":
        acc += int(instruction[1])
    elif instruction[0] == "jmp":
        offset = int(instruction[1])
    elif instruction[0] == "nop":
        pass

    return acc, offset


if __name__ == '__main__':
    instructions = load_data()
    performed_instructions = set()
    loop = False
    acc = 0
    line = 0

    while not loop:
        performed_instructions.add(line)
        acc_mod, offset = perform_instruction(instructions[line])
        acc += acc_mod
        line += offset
        if line in performed_instructions:
            loop = True

    print(acc)
