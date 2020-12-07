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


def contains_bags(outer_bag):
    inner_bags = rules[outer_bag]
    contained_bags = 0
    for bag in inner_bags:
        if bag != "no other bags.":
            desc = bag.split(" ")
            nbr_of_bags = int(desc[0])

            sep = " "
            bag_type_desc = [desc[1], desc[2], "bags"]
            bag_type = sep.join(bag_type_desc)

            nbr_contained = contains_bags(bag_type)

            contained_bags += nbr_of_bags * (1 + nbr_contained)
    return contained_bags


if __name__ == '__main__':
    rules_list = load_data()
    rules = compile_rules(rules_list)

    bags_in_gold_bag = contains_bags("shiny gold bags")
    print(bags_in_gold_bag)
