def load_data():
    input_object = open("input.txt", "r")
    input_data = input_object.read()
    input_object.close()

    separated_data = input_data.split("\n\n")
    cleaned_data = []

    for line in separated_data:
        cleaned_data.append(line.replace("\n", " "))

    return cleaned_data


def passport_valid(passport):
    passport_fields = passport.strip().split(" ")
    passport_dict = {}
    for field in passport_fields:
        value = field.split(":")
        passport_dict[value[0]] = value[1]

    mandatory_keys = ("eyr", "byr", "iyr", "hgt", "hcl", "ecl", "pid")

    valid = all(key in passport_dict for key in mandatory_keys)

    return valid


if __name__ == '__main__':
    passport_list = load_data()
    valid_passports = 0
    for passport in passport_list:
        if passport_valid(passport):
            valid_passports += 1

    print(valid_passports)
