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


def descend_slope(slope, step_length, speed):
    slope_width = len(slope[0])
    nbr_trees = 0
    x = 0
    for line in slope[::speed]:
        if x > slope_width - 1:
            x = x - slope_width
        if line[x] == "#":
            nbr_trees += 1
        x = x + step_length
    return nbr_trees


def multiply_trees():
    product = descend_slope(slope, 1, 1) * descend_slope(slope, 3, 1) * descend_slope(slope, 5, 1) * descend_slope(slope, 7, 1) * descend_slope(slope, 1, 2)
    print(product)


if __name__ == '__main__':
    slope = generate_slope()
    multiply_trees()
