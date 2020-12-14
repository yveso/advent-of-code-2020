with open("../inputs/12.txt") as file:
    actions = [line.strip() for line in file]

east_distance, north_distance = 0, 0
waypoint_east, waypoint_north = 10, 1

for action in actions:
    code, ammount = action[0], int(action[1:])

    if code in "EW":
        waypoint_east += (1 if code == "E" else -1) * ammount
    elif code in "SN":
        waypoint_north += (1 if code == "N" else -1) * ammount
    elif code == "R":
        if ammount == 90:
            waypoint_east, waypoint_north = waypoint_north, -waypoint_east
        elif ammount == 180:
            waypoint_east, waypoint_north = -waypoint_east, -waypoint_north
        elif ammount == 270:
            waypoint_east, waypoint_north = -waypoint_north, waypoint_east
    elif code == "L":
        if ammount == 90:
            waypoint_east, waypoint_north = -waypoint_north, waypoint_east
        elif ammount == 180:
            waypoint_east, waypoint_north = -waypoint_east, -waypoint_north
        elif ammount == 270:
            waypoint_east, waypoint_north = waypoint_north, -waypoint_east
    elif code == "F":
        east_distance += ammount * waypoint_east
        north_distance += ammount * waypoint_north

manhattan_distance = abs(east_distance) + abs(north_distance)

print(f"The answer is {manhattan_distance}")
