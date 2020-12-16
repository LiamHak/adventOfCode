def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()
    ticket_list = [line.strip() for line in input_data]

    my_ticket = []
    nearby_tickets = []
    ranges = []

    data_zone = "ranges"
    for line in ticket_list:
        if line:

            if line.split(":")[0] == "your ticket":
                data_zone = "mine"
                continue
            elif line.split(":")[0] == "nearby tickets":
                data_zone = "nearby"
                continue

            if data_zone == "ranges":
                ranges.append(line.split(":"))
            elif data_zone == "mine":
                my_ticket = [int(i) for i in line.split(",")]
            elif data_zone == "nearby":
                nearby_tickets.append([int(i) for i in line.split(",")])

    return ranges, my_ticket, nearby_tickets


def get_valid_ranges(ranges_list):
    numbers = set()
    for line in ranges_list:
        ranges = line[1].split(" or ")
        for val_range in ranges:
            bounds = val_range.split("-")
            lower = int(bounds[0])
            higher = int(bounds[1])
            for i in range(lower, higher + 1):
                numbers.add(i)
    return numbers


if __name__ == '__main__':
    ranges, my_ticket, nearby_tickets = load_data()
    valid_numbers = get_valid_ranges(ranges)
    error_rate = 0

    for ticket in nearby_tickets:
        for value in ticket:
            if int(value) not in valid_numbers:
                error_rate += int(value)

    print(error_rate)

