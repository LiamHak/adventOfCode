input_object = open("input.txt", "r")
input_data = input_object.readlines()

nbr_valid = 0

for line in input_data:
    data = line.split(" ")
    range_list = data[0].split("-")
    nbr_range = []
    for nbr in range_list:
        nbr_range.append(int(nbr))

    letter = data[1].strip(":")

    pw = data[2]
    pw_chars = [char for char in pw]
    pw_count = pw_chars.count(letter)
    if nbr_range[0] <= pw_count <= nbr_range[1]:
        nbr_valid += 1


print(nbr_valid)