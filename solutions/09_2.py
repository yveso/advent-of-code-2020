with open("../inputs/09.txt") as file:
    numbers = [int(line.strip()) for line in file]


def search(numbers, answer_to_check):
    for i, lower_bound in enumerate(numbers[:-1]):
        for j, _ in enumerate(numbers[i + 1 :]):
            current_contiguous_set = numbers[i : i + j + 2]
            if sum(current_contiguous_set) == answer_to_check:
                return min(current_contiguous_set) + max(current_contiguous_set)


answer_from_part_one = 1721308972
answer = search(numbers, answer_from_part_one)

print(f"The answer is {answer}")
