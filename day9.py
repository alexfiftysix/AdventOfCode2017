def part1(stream):
    next_is_invalid = False
    angle_brace_open = False
    open_curly_braces = 0
    group_count = 0
    score = 0

    for char in stream:
        if next_is_invalid:
            next_is_invalid = False
        elif angle_brace_open:
            if char == ">":
                angle_brace_open = False
        elif char == "!":
            next_is_invalid = True
        elif char == "<":
            angle_brace_open = True
        elif char == "{":
            open_curly_braces += 1
        elif char == "}" and open_curly_braces > 0:
            group_count += 1
            score += open_curly_braces
            open_curly_braces -= 1

    return group_count, score


file = open('day_9_input.txt', 'r')
in_stream = file.read().strip()
file.close()


print(part1(in_stream))

# last answer: 3721
