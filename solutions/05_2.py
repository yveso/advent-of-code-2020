with open("../inputs/05.txt") as file:
    passes = [line.strip() for line in file]


def get_row(row_codes):
    rows = list(range(128))
    for code in row_codes:
        if code == "F":
            rows = rows[: len(rows) // 2]
        elif code == "B":
            rows = rows[len(rows) // 2 :]
    return rows[0]


def get_column(col_codes):
    cols = list(range(8))
    for code in col_codes:
        cols = cols[: len(cols) // 2] if code == "L" else cols[len(cols) // 2 :]
    return cols[0]


seat_ids = [get_row(p[:7]) * 8 + get_column(p[-3:]) for p in passes]
my_id = list(set(range(min(seat_ids), max(seat_ids) + 1)) - set(seat_ids))[0]

print(f"The answer is {my_id}")
