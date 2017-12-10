import operator

ops = {
    "==": operator.eq,
    ">=": operator.ge,
    ">": operator.gt,
    "<": operator.lt,
    "<=": operator.le,
    "!=": operator.ne
}

file_name = 'day8_input.txt'
file = open(file_name, 'r')

registers = {}
# name : amount

max_value = -9999999999999  # dodgy way to make a small starting number, should really not exist at all at this point

while True:
    x = file.readline().strip()

    if x == '':  # If we've reached the end of the file, stop reading
        file.close()
        break

    # If the register hasn't come up yet
    instruction = x.split()

    register = instruction[0]
    comparison_register = instruction[4]
    command = instruction[1]
    operator = ops[instruction[5]]
    comparison_num = int(instruction[6])

    if command == 'dec':  # reverse sign if dec, keep same if inc
        num = int(instruction[2]) * -1
    else:
        num = int(instruction[2])

    if register not in registers.keys():  # Add new registers
        registers[register] = 0

    if comparison_register not in registers.keys():
        registers[comparison_register] = 0

    if operator(registers[comparison_register], comparison_num):
        registers[register] += num

    if registers[register] > max_value:
        max_value = registers[register]

        # print('' + x + '')

print(max(registers.values()))
print(max_value)
