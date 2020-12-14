with open("../inputs/12.txt") as file:
    actions = [line.strip() for line in file]

east_distance, north_distance = 0, 0
facing_angle = 0

for action in actions:
    code, ammount = action[0], int(action[1:])

    if code in "EW":
        east_distance += (1 if code == "E" else -1) * ammount
    elif code in "SN":
        north_distance += (1 if code == "N" else -1) * ammount
    elif code in "RL":
        facing_angle = (facing_angle + (1 if code == "R" else -1) * ammount) % 360
    elif code == "F":
        if facing_angle in (0, 180):
            east_distance += (1 if facing_angle == 0 else -1) * ammount
        elif facing_angle in (90, 270):
            north_distance += (1 if facing_angle == 270 else -1) * ammount

manhattan_distance = abs(east_distance) + abs(north_distance)

print(f"The answer is {manhattan_distance}")
