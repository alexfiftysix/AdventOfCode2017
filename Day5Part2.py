test_input = "0\n3\n0\n1\n-3"

file = open('Day5Input.txt', 'r')
numbers = file.read()
file.close()

in_list = numbers.split()
in_list = [int(x) for x in in_list]


current_index = 0
steps = 0
offset = 0

while True:
    try:
        offset = in_list[current_index]
    except IndexError:
        print(steps)
        break

    if in_list[current_index] >= 3:
        in_list[current_index] -= 1
    else:
        in_list[current_index] += 1

    current_index += offset
    steps += 1
