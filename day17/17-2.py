def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    input_data = [[char for char in line.strip()] for line in input_data]

    return input_data


def step(grid):
    new_grid = {}
    for x in range(min(key[0] for key in grid.keys()) - 1, max(key[0] for key in grid.keys()) + 2):
        for y in range(min(key[1] for key in grid.keys()) - 1, max(key[1] for key in grid.keys()) + 2):
            for z in range(min(key[2] for key in grid.keys()) - 1, max(key[2] for key in grid.keys()) + 2):
                for q in range(min(key[3] for key in grid.keys()) - 1, max(key[3] for key in grid.keys()) + 2):
                    active = grid.get((x, y, z, q), False)
                    active_neighbors = 0
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            for dz in (-1, 0, 1):
                                for dq in (-1, 0, 1):
                                    if dx == dy == dz == dq == 0:
                                        continue
                                    if grid.get((x + dx, y + dy, z + dz, q + dq), False):
                                        active_neighbors += 1
                    if (active and active_neighbors in (2, 3)) or (not active and active_neighbors == 3):
                        new_grid[(x, y, z, q)] = True
    return new_grid


if __name__ == '__main__':
    starting_slice = load_data()
    grid = {}
    for row, line in enumerate(starting_slice):
        for col, ch in enumerate(line):
            grid[(row, col, 0, 0)] = ch == '#'

    for i in range(6):
        print(i, sum(grid.values()))
        grid = step(grid)
    print(sum(grid.values()))
