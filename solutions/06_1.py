with open("../inputs/06.txt") as file:
    lines = [line.strip() for line in file]

group_answers = []
answers = set()
for line in lines:
    if line:
        answers.update(set(line))
    else:
        group_answers.append(len(answers))
        answers.clear()
else:
    group_answers.append(len(answers))

print(f"The answer is {sum(group_answers)}")
