def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    rows = []
    for line in input_data:
        rows.append([char for char in line.replace("\n", "")])

    return rows


def check_diagonals(i, j, seats):
    directions = ["r", "l", "u", "d", "ul", "ur", "dl", "dr"]
    nbr_rows = len(seats)
    nbr_cols = len(seats[0])
    nbr_occupied_seen = 0
    for dir in directions:
        if dir == "r":
            x, y = 0, 1
        elif dir == "l":
            x, y = 0, -1
        elif dir == "u":
            x, y = -1, 0
        elif dir == "d":
            x, y = 1, 0
        elif dir == "ur":
            x, y = -1, 1
        elif dir == "ul":
            x, y = -1, -1
        elif dir == "dr":
            x, y = 1, 1
        elif dir == "dl":
            x, y = 1, -1

        for distance in range(1, max(nbr_rows, nbr_cols)):
            x_dist = x * distance
            y_dist = y * distance
            if i + x_dist < 0 or i + x_dist >= nbr_rows or j + y_dist < 0 or j + y_dist >= nbr_cols:
                break
            if seats[i + x_dist][j + y_dist] == "#":
                nbr_occupied_seen += 1
                break
            if seats[i + x_dist][j + y_dist] == "L":
                break
    return nbr_occupied_seen


def perform_iteration(seats):
    new_seats = []

    for i, row in enumerate(seats):
        new_row = []
        for j, seat in enumerate(row):

            if seats[i][j] == ".":
                new_row.append(".")

            nbr_occupied_seen = check_diagonals(i, j, seats)
            if seats[i][j] == "L":
                if nbr_occupied_seen == 0:
                    new_row.append("#")
                else:
                    new_row.append("L")
            elif seats[i][j] == "#":
                if nbr_occupied_seen >= 5:
                    new_row.append("L")
                else:
                    new_row.append("#")
        new_seats.append(new_row)
    return new_seats


def count_occupied(seats):
    nbr_occupied = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                nbr_occupied += 1
    return nbr_occupied


if __name__ == '__main__':
    seats = load_data()

    steady_state = False
    iterator = 1
    while not steady_state:
        print(iterator)
        new_seats = perform_iteration(seats)
        steady_state = True
        for i in range(0, len(seats)):
            for j in range(0, len(seats[0])):
                steady_state = steady_state and (seats[i][j] == new_seats[i][j])
        seats = new_seats
        iterator += 1

    nbr_occupied = count_occupied(seats)
    print(nbr_occupied)
