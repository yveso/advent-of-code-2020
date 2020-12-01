with open("../inputs/01.txt") as file:
    entries = [int(line.strip()) for line in file]


def search_answer():
    for i, first_entry in enumerate(entries):
        for j, second_entry in enumerate(entries[i + 1 :]):
            for third_entry in entries[i + j + 1 :]:
                if first_entry + second_entry + third_entry == 2020:
                    return first_entry * second_entry * third_entry


print(f"The answer is {search_answer()}")
