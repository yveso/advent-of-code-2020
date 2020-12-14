with open("../inputs/13.txt") as file:
    timestamp = int(file.readline())
    bus_ids = [int(id) for id in file.readline().split(",") if id != "x"]

print(timestamp, bus_ids)

bus_ids_with_waiting_time = [
    (bus_id, bus_id - timestamp % bus_id) for bus_id in bus_ids
]

fastest = sorted(bus_ids_with_waiting_time, key=lambda x: x[1])[0]

answer = fastest[0] * fastest[1]

print(f"The answer is {answer}")
