from operator import add


def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    directions = []
    for line in input_data:
        cleaned_line = line.replace("\n", "")
        line_length = len(cleaned_line)
        entry = [cleaned_line[0], int(cleaned_line[1:line_length])]
        directions.append(entry)

    return directions


def rotate(rot, facing, val):
    if rot == "L":
        facing -= val
    elif rot == "R":
        facing += val

    if facing >= 360:
        facing -= 360
    elif facing < 0:
        facing += 360

    return facing


def get_direction(facing):
    direc = ""
    if facing == 0:
        direc = "E"
    elif facing == 90:
        direc = "S"
    elif facing == 180:
        direc = "W"
    elif facing == 270:
        direc = "N"
    return direc


def move_one_step(step, facing):
    change = [0, 0, facing]
    direc = step[0]
    value = step[1]

    if direc == "F":
        direc = get_direction(facing)

    if direc == "L" or direc == "R":
        change[2] = rotate(direc, facing, value)
    elif direc == "N":
        change[1] = value
    elif direc == "S":
        change[1] = -value
    elif direc == "E":
        change[0] = value
    elif direc == "W":
        change[0] = -value

    return change


if __name__ == '__main__':
    directions = load_data()
    location = [0, 0, 0]
    for step in directions:
        change = move_one_step(step, location[2])
        location[0:2] = list(map(add, location[0:2], change[0:2]))
        location[2] = change[2]
    manhattan_dist = abs(location[0]) + abs(location[1])

    print(manhattan_dist)
