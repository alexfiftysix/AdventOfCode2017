puzzle_file = open('Day4_input.txt', 'r')

counter = 0

while True:

    current_line = puzzle_file.readline()

    if current_line == '':
        break

    current_line_list = current_line.split()
    print(current_line_list)

    s = list(set(current_line_list))
    s.sort()
    current_line_list.sort()

    if s == current_line_list:
        counter += 1

    print(counter)

puzzle_file.close()
