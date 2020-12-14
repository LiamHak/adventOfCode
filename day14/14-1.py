def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    instructions = []
    for line in input_data:
        line2 = line.split(" = ")
        instructions.append([line2[0], line2[1].strip("\n")])

    return instructions


def apply_mask(num, mask):
    bit_num = bin(num)[2:].zfill(36)

    new_bit_num = ""
    for i, bit in enumerate(bit_num):
        if mask[i] == "X":
            new_bit_num += bit
        else:
            new_bit_num += mask[i]
    bit_num = new_bit_num
    return bit_num


if __name__ == '__main__':
    instructions = load_data()
    mem = dict()
    mask = ""

    for inst in instructions:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            bit_num = apply_mask(int(inst[1]), mask)
            mem_adress = int(inst[0].strip("mem[").strip("]"))
            mem[mem_adress] = int(bit_num, 2)

    total_memory_values = sum(mem.values())

    print(total_memory_values)
