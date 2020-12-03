with open("../inputs/03.txt") as file:
    rows = [line.strip() for line in file]


def count_trees(move_right, move_down):
    positions = (
        row[(i * move_right) % len(row)] for i, row in enumerate(rows[::move_down])
    )
    count = len([position for position in positions if position == "#"])
    return count


answer = (
    count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2)
)

print(f"The answer is {answer}")
