from common.computer import Computer
from copy import deepcopy


def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()

    cleaned_data = []

    for line in input_data:
        cleaned_data.append(line.replace("\n", "").split(" "))

    return cleaned_data


def task_one():
    instructions = load_data()
    computer = Computer(instructions)
    performed_instructions = set()
    loop = False
    index = computer.get_instruction_index()

    while not loop:
        performed_instructions.add(index)
        computer.run_one_instruction()
        index = computer.get_instruction_index()
        if index in performed_instructions:
            loop = True
    acc = computer.get_accumulator()

    print("Accumulator value before loop:", acc)


def task_two():
    instructions = load_data()
    nbr_instructions = len(instructions)

    for i in range(nbr_instructions):
        loop_resolved = False

        new_instructions = deepcopy(instructions)
        if instructions[i][0] == "jmp":
            new_instructions[i][0] = "nop"
        elif instructions[i][0] == "nop":
            new_instructions[i][0] = "jmp"

        computer = Computer(new_instructions)

        performed_instructions = set()
        loop = False
        index = 0

        while not loop:
            performed_instructions.add(index)
            computer.run_one_instruction()
            index = computer.get_instruction_index()
            if index in performed_instructions:
                loop = True
            elif index >= nbr_instructions:
                loop_resolved = True
                break
        if loop_resolved:
            break

    acc = computer.get_accumulator()
    print("Accumulator value after finished program:", acc)


if __name__ == '__main__':
    task_one()
    task_two()



