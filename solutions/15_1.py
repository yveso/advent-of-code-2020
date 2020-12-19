spoken_numbers = [2, 1, 10, 11, 0, 6]
turns = 2020

for turn in range(len(spoken_numbers), turns):
    turn += 1
    last_number = spoken_numbers[-1]

    if last_number not in spoken_numbers[:-2]:
        spoken_numbers.append(0)
    else:
        last_time_spoken = len(spoken_numbers[:-1]) - list(
            reversed(spoken_numbers[:-1])
        ).index(last_number)
        spoken_numbers.append(turn - 1 - last_time_spoken)


answer = spoken_numbers[-1]
print(f"The answer is {answer}")
