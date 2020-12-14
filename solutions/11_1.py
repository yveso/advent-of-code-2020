with open("../inputs/11.txt") as file:
    grid = [list(line.strip()) for line in file]


def count_occupied_adjacent_seats(grid, row, col):
    row_border, col_border = len(grid) - 1, len(grid[0]) - 1
    count = 0
    if col > 0 and row > 0 and grid[row - 1][col - 1] == "#":
        count += 1
    if row > 0 and grid[row - 1][col] == "#":
        count += 1
    if col < col_border and row > 0 and grid[row - 1][col + 1] == "#":
        count += 1
    if col > 0 and grid[row][col - 1] == "#":
        count += 1
    if col < col_border and grid[row][col + 1] == "#":
        count += 1
    if col > 0 and row < row_border and grid[row + 1][col - 1] == "#":
        count += 1
    if row < row_border and grid[row + 1][col] == "#":
        count += 1
    if col < col_border and row < row_border and grid[row + 1][col + 1] == "#":
        count += 1

    return count


def next_grid(old_grid):
    new_grid = []
    for r, row in enumerate(old_grid):
        new_row = []
        for c, seat in enumerate(row):
            new_seat = ""
            occupied_adjacent = count_occupied_adjacent_seats(old_grid, r, c)
            if seat == "L" and occupied_adjacent == 0:
                new_seat = "#"
            elif seat == "#" and occupied_adjacent >= 4:
                new_seat = "L"
            else:
                new_seat = seat
            new_row.append(new_seat)
        new_grid.append(new_row)
    return new_grid


while True:
    ng = next_grid(grid)
    if ng == grid:
        break
    grid = ng

answer = sum(row.count("#") for row in grid)
print(f"The answer is {answer}")
