input_object = open("input.txt", "r")
input_data = input_object.readlines()

nbr_valid = 0

for line in input_data:
    data = line.split(" ")
    range_list = data[0].split("-")
    nbr_places = []
    for nbr in range_list:
        nbr_places.append(int(nbr))

    letter = data[1].strip(":")

    pw = data[2]
    pw_chars = [char for char in pw]
    if (pw_chars[nbr_places[0]-1] == letter) != (pw_chars[nbr_places[1]-1] == letter):
        nbr_valid += 1

print(nbr_valid)
