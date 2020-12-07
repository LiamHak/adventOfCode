def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.read()
    input_object.close()

    return input_data.split("\n")


def compile_rules(rules_list):
    rules = dict()
    for rule in rules_list:
        if rule:
            rule = rule.split(" contain ")
            outer_bag = rule[0]
            inner_bags = rule[1].split(", ")
            rules[outer_bag] = inner_bags
    return rules


def contains_gold_bag(outer_bag):
    inner_bags = rules[outer_bag]
    contains_gold = False

    for bag in inner_bags:
        if bag != "no other bags.":
            desc = bag.split(" ")
            if desc[1] == "shiny" and desc[2] == "gold":
                contains_gold = True
                break
            else:
                sep = " "
                bag_type_desc = [desc[1], desc[2], "bags"]
                bag_type = sep.join(bag_type_desc)
                contains_gold = contains_gold_bag(bag_type)
                if contains_gold:
                    break
    return contains_gold


if __name__ == '__main__':
    rules_list = load_data()
    rules = compile_rules(rules_list)

    gold_bags = 0

    for bag in rules.keys():
        if contains_gold_bag(bag):
            gold_bags += 1

    print(gold_bags)
