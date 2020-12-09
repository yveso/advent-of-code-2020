with open("../inputs/09.txt") as file:
    numbers = [int(line.strip()) for line in file]


def search_first_non_summable(numbers, preamble_length):
    for i, current_number in enumerate(numbers[preamble_length : -preamble_length + 1]):
        numbers_before = numbers[i : i + preamble_length]

        for j, first_summand in enumerate(numbers_before[:-1]):
            second_summands = numbers_before[j + 1 :]
            we_have_a_sum = any(
                first_summand + second == current_number for second in second_summands
            )
            if we_have_a_sum:
                break
        else:
            return current_number


answer = search_first_non_summable(numbers, 25)

print(f"The answer is {answer}")
