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
    masks = all_masks(mask)
    results = []
    for old_mask in masks:
        bit_num = bin(num)[2:].zfill(36)
        new_bit_num = [bit if old_mask[i] == "X" else old_mask[i] for i, bit in enumerate(bit_num)]
        bit_num = "".join(new_bit_num)
        results.append(bit_num)

    return results


def all_masks(mask):
    if not mask:
        yield ''
        return
    for m in all_masks(mask[1:]):
        if mask[0] == '0':
            yield 'X' + m  # leave unchanged
        elif mask[0] == '1':
            yield '1' + m  # replace with 1
        elif mask[0] == 'X':
            yield '0' + m  # replace with 0
            yield '1' + m  # replace with 1


if __name__ == '__main__':
    instructions = load_data()
    mem = dict()
    mask = ""

    for inst in instructions:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            bit_nums = int(inst[1])
            mem_addresses = apply_mask(int(inst[0].strip("mem[").strip("]")), mask)
            for mem_address in mem_addresses:
                mem[mem_address] = bit_nums

    total_memory_values = sum(mem.values())

    print(total_memory_values)
