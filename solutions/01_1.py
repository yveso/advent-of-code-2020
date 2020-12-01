with open("../inputs/01.txt") as file:
    entries = [int(line.strip()) for line in file]


def search_answer():
    for i, first_entry in enumerate(entries):
        for second_entry in entries[i + 1 :]:
            if first_entry + second_entry == 2020:
                return first_entry * second_entry


print(f"The answer is {search_answer()}")
