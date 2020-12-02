with open("../inputs/02.txt") as file:
    entries = [line.strip() for line in file]

count_valid_passwords = 0

for entry in entries:
    min_max_amount, letter, password = entry.split()
    min_amount, max_amount = [int(x) for x in min_max_amount.split("-")]
    letter = letter[0]

    if min_amount <= password.count(letter) <= max_amount:
        count_valid_passwords += 1

print(f"The answer is {count_valid_passwords}")
