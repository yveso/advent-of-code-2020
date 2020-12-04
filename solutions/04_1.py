with open("../inputs/04.txt") as file:
    lines = [line.strip() for line in file]

count_valid_passports, count_fields, has_cid = 0, 0, False

for line in lines:
    if line:
        count_fields += len(line.split())
        if not has_cid:
            has_cid = "cid" in line
    else:
        if count_fields == 8 or (count_fields == 7 and not has_cid):
            count_valid_passports += 1
        count_fields, has_cid = 0, False

print(f"The answer is {count_valid_passports}")
