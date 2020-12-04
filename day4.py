import functools 
import re

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_byr_value(value):    
    return valid_simple_numeric_value(int(value), 1920, 2002)

def valid_iyr_value(value):
    return valid_simple_numeric_value(int(value), 2010, 2020)

def valid_eyr_value(value):
    return valid_simple_numeric_value(int(value), 2020, 2030)

def valid_hgt_value(value):
    if ( value.endswith("in")):
        return valid_simple_numeric_value(int(value[0:len(value)-2]), 59, 76)
    elif (value.endswith("cm")):
        return valid_simple_numeric_value(int(value[0:len(value)-2]), 150, 193)

def valid_hcl_value(value):    
    x = re.findall("^#([a-f0-9]{6})", value)
    if x:
        return True
    return False

def valid_ecl_value(value):
    return value in eye_colors

def valid_pid_value(value):
    return len(value) == 9 and value.isdigit()

validate_functions = {
    'byr': valid_byr_value,
    'iyr': valid_iyr_value,
    'eyr': valid_eyr_value,
    'hgt': valid_hgt_value,
    'hcl': valid_hcl_value,
    'ecl': valid_ecl_value,
    'pid': valid_pid_value
}

def replace_newline_with_space(line):
    return line.replace('\n', ' ') 

def contains_all_fields(line):
    return all( field in line for field in mandatory_fields )

def validate_all(line):
    if not all( field in line for field in mandatory_fields ):
        return False
    
    json_obj = from_line_to_json(line)
    print(json_obj)

    for field in mandatory_fields:
        if not validate_functions[field](json_obj[field]):
            return False
    return True

def from_line_to_json(line):
    fields_and_values = line.split(' ')
    object = {}
    for data in fields_and_values:
        field_and_value = data.split(':')
        object[field_and_value[0]] = field_and_value[1]
    return object


def valid_simple_numeric_value(value, min, max):
    return value >= min and value <= max

text_file = open("passport.txt", "r")
map_lines = text_file.read().split('\n\n')
map_lines = list(map(replace_newline_with_space, map_lines))
valid_passports_part1 = list(map(contains_all_fields, map_lines))

valid_passports_part2 = list(map(validate_all, map_lines))

print('valid_passports-part1: ', valid_passports_part1.count(True))
print('valid_passports-part2: ', valid_passports_part2.count(True))