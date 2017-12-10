def find_max_index(list_of_ints):
    index = 0
    x = max(list_of_ints)
    while True:
        for i in memory_bank:
            if i == x:
                return index
            else:
                index += 1


test_case = '0 2 7 0'
day_6_input = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'

counter = 0
memory_bank = day_6_input.split()
memory_bank = [int(x) for x in memory_bank]

all_configurations = [memory_bank[:]]

while True:
    max_index = find_max_index(memory_bank)
    max_no = memory_bank[max_index]

    memory_bank[max_index] = 0
    current_index = max_index

    for i in range(max_no):
        current_index += 1
        try:
            memory_bank[current_index]
        except IndexError:
            current_index = 0
        memory_bank[current_index] += 1
    counter += 1

    if memory_bank in all_configurations:
        all_configurations.append(memory_bank[:])
        print(memory_bank)
        print(all_configurations)
        break
    else:
        all_configurations.append(memory_bank[:])

x_counter = 0
y_counter = 0
for x in all_configurations:
    for y in all_configurations:
        if x == y and x_counter != y_counter:
            print(x, y, x == y)
            print(abs(x_counter-y_counter))
        y_counter += 1
    y_counter = 0
    x_counter += 1
