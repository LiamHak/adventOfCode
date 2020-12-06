import gh

def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.read()
    input_object.close()

    separated_data = input_data.split("\n\n")

    return separated_data


def count_declared_items(declaration):
    individual_declarations = declaration.split("\n")
    set_list = list()

    common_items = set(individual_declarations[0])
    for dec in individual_declarations:
        if dec:
            dec_set = set(dec)
            set_list.append(dec_set)
            common_items = common_items.intersection(dec_set)

    return len(common_items)


if __name__ == '__main__':
    declaration_list = load_data()
    results = list()

    item_sum = 0
    for dec in declaration_list:
        result = count_declared_items(dec)
        results.append(result)
        item_sum += result

    print(item_sum)
