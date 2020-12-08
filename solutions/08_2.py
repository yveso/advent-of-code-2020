with open("../inputs/08.txt") as file:
    instructions = [line.strip() for line in file]


def run(instructions_to_run):
    accumulator, instruction_index = 0, 0
    executed_indexes = []

    while True:
        if instruction_index in executed_indexes:
            return None

        executed_indexes.append(instruction_index)
        operation, argument = instructions_to_run[instruction_index].split()

        if operation == "acc":
            accumulator += int(argument)
            instruction_index += 1
        elif operation == "nop":
            instruction_index += 1
        elif operation == "jmp":
            instruction_index += int(argument)

        if instruction_index == len(instructions_to_run):
            return accumulator


answer = 0
for i, instruction in enumerate(instructions):
    operation, argument = instruction.split()
    if operation == "acc":
        continue

    modified_instructions = (
        instructions[:i]
        + [f"{'nop' if operation == 'jmp' else 'jmp'} {argument}"]
        + instructions[i + 1 :]
    )
    answer = run(modified_instructions)
    if answer:
        break

print(f"The answer is {answer}")
