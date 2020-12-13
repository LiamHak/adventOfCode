def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.readlines()
    input_object.close()

    earliest_dep = int(input_data[0])

    busses = input_data[1].split(",")

    return earliest_dep, busses


if __name__ == '__main__':
    earliest_dep, busses = load_data()
    dep_times = dict()
    for bus in busses:
        if not bus == "x":
            bus_id = int(bus)
            dep_found = False
            coeff = 1
            while not dep_found:
                dep_time = bus_id * coeff
                if dep_time > earliest_dep:
                    dep_times[dep_time] = bus_id
                    dep_found = True
                coeff += 1
    best_dep = min(dep_times.keys())
    diff = best_dep - earliest_dep
    id = dep_times[best_dep]

    prod = diff*id

    print(prod)
