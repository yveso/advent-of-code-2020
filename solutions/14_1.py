with open("../inputs/14.txt") as file:
    programm = [line.strip() for line in file]

memory = {}
current_mask = ""

for line in programm:
    instruction, value = line.split(" = ")
    if instruction == "mask":
        current_mask = value
    else:
        memory_address = instruction[4:-1]
        value_bin = f"{int(value):036b}"
        output_bin = "".join(
            v if m == "X" else m for v, m in zip(value_bin, current_mask)
        )
        output_dec = int(output_bin, 2)
        memory[memory_address] = output_dec


answer = sum(memory.values())
print(f"The answer is {answer}")
