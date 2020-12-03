def generate_slope():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    slope = []

    for line in input_data:
        stripped_line = line.strip()
        char_array = [char for char in stripped_line]
        slope.append(char_array)
    return slope


def descend_slope(slope):
    slope_length = len(slope)
    slope_width = len(slope[0])
    nbr_trees = 0
    step_length = 3
    x = 0
    for line in slope:

        if x > slope_width - 1:
            x = x - slope_width
        if line[x] == "#":
            line[x] = "X"
            nbr_trees += 1
        else:
            line[x] = "O"
        print(line)
        x = x + step_length
    print(nbr_trees)


if __name__ == '__main__':
    slope = generate_slope()
    descend_slope(slope)
