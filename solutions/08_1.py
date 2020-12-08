with open("../inputs/08.txt") as file:
    instructions = [line.strip() for line in file]

accumulator, instruction_index = 0, 0
executed_indexes = []

while True:
    if instruction_index in executed_indexes:
        break

    executed_indexes.append(instruction_index)
    operation, argument = instructions[instruction_index].split()

    if operation == "acc":
        accumulator += int(argument)
        instruction_index += 1
    elif operation == "nop":
        instruction_index += 1
    elif operation == "jmp":
        instruction_index += int(argument)

print(f"The answer is {accumulator}")
