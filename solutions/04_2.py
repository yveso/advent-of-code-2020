with open("../inputs/04.txt") as file:
    lines = [line.strip() for line in file]


def check_field(field):
    key, value = field
    rules = {
        "byr": lambda v: all(c.isnumeric() for c in v) and (1920 <= int(v) <= 2002),
        "iyr": lambda v: all(c.isnumeric() for c in v) and (2010 <= int(v) <= 2020),
        "eyr": lambda v: all(c.isnumeric() for c in v) and (2020 <= int(v) <= 2030),
        "hgt": lambda v: (
            (
                v[-2:] == "cm"
                and all(c.isnumeric() for c in v[:-2])
                and (150 <= int(v[:-2]) <= 193)
            )
            or (
                v[-2:] == "in"
                and all(c.isnumeric() for c in v[:-2])
                and (59 <= int(v[:-2]) <= 76)
            )
        ),
        "hcl": lambda v: (
            len(v) == 7 and v[0] == "#" and all(c in "0123456789abcdef" for c in v[1:])
        ),
        "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda v: len(v) == 9 and all(c.isnumeric() for c in v),
        "cid": lambda v: True,
    }
    return rules.get(key)(value)


passports, passport, count_valid_passports = [], "", 0

for line in lines:
    if line:
        passport += " "
        passport += line
    else:
        count_fields = len(passport.split())
        if count_fields == 8 or (count_fields == 7 and "cid" not in passport):
            passports.append(passport)
        passport = ""

for passport in passports:
    fields = [field.split(":") for field in passport.split()]
    if all(check_field(field) for field in fields):
        count_valid_passports += 1

print(f"The answer is {count_valid_passports}")
