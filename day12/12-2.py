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


if __name__ == '__main__':
    instructions = load_data()
    ship = complex(0, 0)
    waypoint = complex(10, 1)  # offset relative to ship

    for instruction in instructions:
        action, magnitude = instruction[0], int(instruction[1])

        if action == "N":
            waypoint += complex(0, magnitude)
        elif action == "S":
            waypoint += complex(0, -magnitude)
        elif action == "E":
            waypoint += complex(magnitude, 0)
        elif action == "W":
            waypoint += complex(-magnitude, 0)
        elif action == "F":
            ship += waypoint * magnitude
        elif action == "R":
            waypoint *= complex(0, -1) ** (magnitude // 90)
        elif action == "L":
            waypoint *= complex(0, 1) ** (magnitude // 90)
    manhattan_dist = int(abs(ship.real) + abs(ship.imag))

    print(manhattan_dist)
