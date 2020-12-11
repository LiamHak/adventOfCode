from copy import  deepcopy

def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    rows = []
    for line in input_data:
        rows.append([char for char in line.replace("\n", "")])

    return rows


def perform_iteration(seats):
    nbr_rows = len(seats)
    nbr_cols = len(seats[0])

    new_seats = []

    for i, row in enumerate(seats):
        new_row = []
        for j, seat in enumerate(row):
            nbr_occupied_adj = 0

            if seats[i][j] == ".":
                new_row.append(".")

            for x in range(max(0, i-1), min(i+1, nbr_rows-1)+1):
                for y in range(max(0, j-1), min(j+1, nbr_cols-1)+1):
                    if x != i or y != j:
                        if seats[x][y] == "#":
                            nbr_occupied_adj += 1
            if seats[i][j] == "L":
                if nbr_occupied_adj == 0:
                    new_row.append("#")
                else:
                    new_row.append("L")
            elif seats[i][j] == "#":
                if nbr_occupied_adj >= 4:
                    new_row.append("L")
                else:
                    new_row.append("#")
        new_seats.append(new_row)
    return new_seats


def flatten(list):
    flat_list = []
    for sublist in list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


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
