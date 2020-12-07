with open("../inputs/07.txt") as file:
    rules_raw = [line.strip() for line in file]

rules = {}


def check(bag_color):
    if not rules[bag_color]:
        return False
    if "shiny gold" in rules[bag_color]:
        return True

    for color in rules[bag_color]:
        if check(color):
            return True

    return False


for rule in rules_raw:
    key, contents = rule.split(" contain ")
    key = " ".join(key.split()[:2])
    contents = (
        []
        if contents == "no other bags."
        else [" ".join(v.split()[1:3]) for v in contents.split(", ")]
    )
    rules[key] = contents


answer = sum([1 if check(rule[0]) else 0 for rule in rules.items()])
print(f"The answer is {answer}")
