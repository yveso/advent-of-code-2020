with open("../inputs/06.txt") as file:
    lines = [line.strip() for line in file]

group_answers = []
current_answers = []
for line in lines:
    if line:
        current_answers.append(list(line))
    else:
        group_answers.append(current_answers)
        current_answers = []
else:
    group_answers.append(current_answers)

group_counts = [len(set(x[0]).intersection(*x[1:])) for x in group_answers]

print(f"The answer is {sum(group_counts)}")
