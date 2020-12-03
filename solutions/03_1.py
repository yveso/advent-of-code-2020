with open("../inputs/03.txt") as file:
    rows = [line.strip() for line in file]

positions = (row[(i * 3) % len(row)] for i, row in enumerate(rows))
count_trees = len([position for position in positions if position == "#"])

print(f"The answer is {count_trees}")
