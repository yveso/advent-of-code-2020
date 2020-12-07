with open("../inputs/07.txt") as file:
    rules_raw = [line.strip() for line in file]

rules = {}


def count(bag_color):
    if not rules[bag_color]:
        return 0

    counter = 0
    for color, ammount in rules[bag_color]:
        # print(color, ammount)
        counter += ammount + ammount * count(color)

    return counter


for rule in rules_raw:
    key, contents = rule.split(" contain ")
    key = " ".join(key.split()[:2])
    contents = (
        []
        if contents == "no other bags."
        else [
            (" ".join(v.split()[1:3]), int(v.split()[0])) for v in contents.split(", ")
        ]
    )
    rules[key] = contents


answer = count("shiny gold")
print(f"The answer is {answer}")
