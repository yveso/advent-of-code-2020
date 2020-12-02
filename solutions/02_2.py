with open("../inputs/02.txt") as file:
    entries = [line.strip() for line in file]

count_valid_passwords = 0

for entry in entries:
    positions, letter, password = entry.split()
    first_position, second_position = [int(x) - 1 for x in positions.split("-")]
    letter = letter[0]

    if (password[first_position] == letter) ^ (password[second_position] == letter):
        count_valid_passwords += 1

print(f"The answer is {count_valid_passwords}")
