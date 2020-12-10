with open("../inputs/10.txt") as file:
    adapters = [int(line.strip()) for line in file]

adapters = sorted(adapters + [0] + [max(adapters) + 3])
one_jolt_diff, three_jolt_diff = 0, 0

for i, _ in enumerate(adapters[:-1]):
    diff = adapters[i + 1] - adapters[i]
    if diff == 1:
        one_jolt_diff += 1
    elif diff == 3:
        three_jolt_diff += 1

answer = one_jolt_diff * three_jolt_diff
print(f"The answer is {answer}")
