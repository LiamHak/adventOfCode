import re


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
    valid = False
    passport_fields = passport.strip().split(" ")
    passport_dict = {}
    for field in passport_fields:
        value = field.split(":")
        passport_dict[value[0]] = value[1]

    mandatory_keys = ("eyr", "byr", "iyr", "hgt", "hcl", "ecl", "pid")

    if all(key in passport_dict for key in mandatory_keys):
        valid = True
        for (key, value) in passport_dict.items():
            valid = valid and validate_field(key, value)

    return valid


def validate_field(key: str, value: str) -> bool:
    valid = False

    if key == 'byr':  # Birth Year
        value = int(value)
        valid = value in range(1920, 2003)
    elif key == 'iyr':  # Issue Year
        value = int(value)
        valid = value in range(2010, 2021)
    elif key == 'eyr':  # Expiration Year
        value = int(value)
        valid = value in range(2020, 2031)
    elif key == 'hgt':  # Height
        match = re.match(r"([0-9]+):?(cm|in)", value)
        if match:
            matching_characters = match.span()[1]
            if matching_characters == len(value):
                (height, unit) = match.groups()
                if unit == 'cm':
                    valid = int(height) in range(150, 194)
                elif unit == 'in':
                    valid = int(height) in range(59, 77)
    elif key == 'hcl':  # Hair Color
        if value[0] == '#' and len(value) == 7:
            matching_characters = re.match(r"(?:[a-z]|[0-9])+", value[1:7]).span()[1]
            if matching_characters == 6:
                valid = True
    elif key == 'ecl':  # Eye Color
        valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':  # Passport ID
        try:
            int(value)
            valid = len(value) == 9
        except:
            pass
    elif key == 'cid':  # Country ID
        valid = True

    return valid


if __name__ == '__main__':
    passport_list = load_data()
    valid_passports = 0
    for passport in passport_list:
        if passport_valid(passport):
            valid_passports += 1

    print(valid_passports)
