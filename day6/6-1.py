def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.read()
    input_object.close()

    separated_data = input_data.split("\n\n")
    cleaned_data = []

    for line in separated_data:
        cleaned_data.append(line.replace("\n", " ").replace(" ", ""))

    return cleaned_data


def count_declared_items(declaration):
    item_set = set()
    for char in declaration:
        item_set.add(char)
    return len(item_set)


if __name__ == '__main__':
    declaration_list = load_data()
    item_sum = 0
    for dec in declaration_list:
        item_sum += count_declared_items(dec)

    print(item_sum)