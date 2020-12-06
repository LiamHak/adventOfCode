import math

def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()

    cleaned_data = []

    for line in input_data:
        cleaned_data.append(line.strip())

    return cleaned_data


def find_place(boarding_pass):
    place_array = [char for char in boarding_pass]
    upper_bound = 127
    lower_bound = 0
    right_bound = 7
    left_bound = 0

    for char in place_array:
        row_interval = upper_bound - lower_bound
        column_interval = right_bound - left_bound
        if char == 'F':
            upper_bound = upper_bound - math.ceil(row_interval / 2)
        elif char == 'B':
            lower_bound = lower_bound + math.ceil(row_interval / 2)
        elif char == 'L':
            right_bound = right_bound - math.ceil(column_interval / 2)
        elif char == 'R':
            left_bound = left_bound + math.ceil(column_interval / 2)

    assert upper_bound == lower_bound
    assert right_bound == left_bound

    row = upper_bound
    column = right_bound
    seat_id = row*8 + column

    return seat_id


if __name__ == '__main__':
    boarding_passes = load_data()
    seat_set = set()
    for bp in boarding_passes:
        seat_id = find_place(bp)
        seat_set.add(seat_id)
    first_seat = min(seat_set)
    last_seat = max(seat_set)
    for seat in range(first_seat, last_seat):
        if seat not in seat_set:
            print("My seat is:", seat)

