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
        in_list[current_index] += 1
    except IndexError:
        print(steps)
        break

    current_index += in_list[current_index] - 1
    steps += 1
