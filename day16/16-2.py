from functools import reduce


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


def identify_possible_fields(ranges_list, index, tickets):
    numbers_set = set([numbers[index] for numbers in tickets])
    possible_names = set()
    for line in ranges_list:
        range_set = set()
        range_name = line[0]
        ranges = line[1].split(" or ")
        for val_range in ranges:
            bounds = val_range.split("-")
            lower = int(bounds[0])
            higher = int(bounds[1])
            for i in range(lower, higher + 1):
                range_set.add(i)
        if numbers_set.issubset(range_set):
            possible_names.add(range_name)
    return possible_names


def determine_fields(ticket_fields):
    determined_fields = dict()
    while ticket_fields:
        determined_value = ""
        detemined_key = 0
        for key in ticket_fields:
            value_set = ticket_fields[key]
            if len(value_set) == 1:
                determined_value = str(value_set.pop())
                detemined_key = key
                determined_fields[key] = determined_value
                break
        ticket_fields.pop(detemined_key)
        for value in ticket_fields.values():
            value.remove(determined_value)
    return determined_fields


if __name__ == '__main__':
    ranges, my_ticket, nearby_tickets = load_data()
    valid_numbers = get_valid_ranges(ranges)
    valid_tickets = []
    ticket_fields = dict()

    for ticket in nearby_tickets:
        valid = True
        for value in ticket:
            if int(value) not in valid_numbers:
                valid = False
        if valid:
            valid_tickets.append(ticket)

    for field in range(len(valid_tickets[0])):
        ticket_fields[field] = identify_possible_fields(ranges, field, valid_tickets)

    determined_fields = determine_fields(ticket_fields)

    interesting_numbers = []
    for index in determined_fields:
        if determined_fields[index].split(" ")[0] == "departure":
            interesting_numbers.append(my_ticket[index])
    result = reduce((lambda x, y: x*y), interesting_numbers)
    print(result)

