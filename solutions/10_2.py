"""
Permutations can only happen in streaks of 1 jolt diffs.
In a streak the Tribonacci series will give us the count.
"""

with open("../inputs/10.txt") as file:
    adapters = [int(line.strip()) for line in file]


def tribonacci(upper_bound):
    if upper_bound == 0:
        return 1
    if upper_bound < 3:
        return upper_bound
    return (
        tribonacci(upper_bound - 3)
        + tribonacci(upper_bound - 2)
        + tribonacci(upper_bound - 1)
    )


adapters = sorted(adapters + [0] + [max(adapters) + 3])
streak_length, number_of_permutations = 0, 1

for i, _ in enumerate(adapters[:-1]):
    diff = adapters[i + 1] - adapters[i]
    if diff == 1:
        streak_length += 1
    elif diff == 3:
        number_of_permutations *= tribonacci(streak_length)
        streak_length = 0

answer = number_of_permutations
print(f"The answer is {answer}")
