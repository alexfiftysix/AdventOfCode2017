# Ring one          Width 1     (x * 2 - 1)
# 1 added           [1]

# Ring 2            width 3     (x * 2 - 1)
# right 1           [2]         CONSTANT
# up 1              [3]         width - 2
# left 2            [4, 5]      width - 1
# down 2            [6, 7]      width - 1
# right 2           [8, 9]      width - 1

# Ring 3            width 5     (x * 2 - 1)
# right 1           [10]        CONSTANT
# up 3              [11-13]     width - 2
# Left 4            [14-17]     width - 1
# down 4            [18-21]     width - 1
# right 4           [22-25]     width - 1

# Ring 4            width 7     (x * 2 - 1)
# right 1           [26]        CONSTANT
# up 5              [27-31]     width - 2
# left 6            [32-37]     width - 1
# down 6            [38-43]     width - 1
# right 6           [44-49]     width - 1

# Ring 5            width 9     (x * 2 - 1)
# right 1           [50]        CONSTANT
# up 7              [51-57]     width - 2
# left 8            [57-65]     width - 1
# down 8            [66-73]     width - 1
# right 8           [74-81]     width - 1

# width == ring_number * 2 - 1

# Each ring ends on the square of the next odd number
# Ring 1        1**2
# Ring 2        3**2
# Ring 3        5**2


def which_ring(x):
    """Tells you which ring the given integer x belongs to"""
    if x < 1:
        return 0
    iter = 1
    while True:
        if x <= (iter * 2 - 1) ** 2:
            return iter
        iter += 1


def make_simple_spiral(x):
    """
    Make a simple spiral up to the integer x
    Simple spiral does not have co-ordinates, but has rings instead
    """
    spiral = {}
    for i in range(x):
        spiral[(which_ring(i), i)] = i
    return spiral


def move(start_pos, direction):
    """
    Move one place in the given direction
    L: left
    R: right
    U: up
    D: down
    :param start_pos: Tuple(int, int): Starting position
    :param direction: direction to move in [L, R, U, D]
    """
    x, y = start_pos

    if direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    end_pos = (x, y)
    return end_pos


def move_around_spiral(start_pos, ring_no):
    width = ring_no * 2 - 1
    current_pos = start_pos

    # move right 1
    current_pos = move(current_pos, "R")

    # Move up width-2
    for x in range(width - 2):
        current_pos = move(current_pos, 'U')

    # Move left width-1
    for x in range(width - 1):
        current_pos = move(current_pos, 'L')

    # Move down width-1
    for x in range(width - 1):
        current_pos = move(current_pos, 'D')

    # Move right width-1
    for x in range(width - 1):
        current_pos = move(current_pos, 'R')

    return current_pos


def generate_spiral(rings):
    """ How many rings the spiral should have"""

    current_num = 1
    current_pos = (0, 0)
    spiral = {current_num: current_pos}

    if rings == 1:
        return spiral

    # Only go on if more than one ring
    for x in range(2, rings + 1):
        width = x * 2 - 1

        # move right 1
        current_pos = move(current_pos, "R")
        current_num += 1
        spiral[current_num] = current_pos

        # Move up width-2
        for y in range(width - 2):
            current_pos = move(current_pos, 'U')
            current_num += 1
            spiral[current_num] = current_pos

        # Move left width-1
        for y in range(width - 1):
            current_pos = move(current_pos, 'L')
            current_num += 1
            spiral[current_num] = current_pos

        # Move down width-1
        for y in range(width - 1):
            current_pos = move(current_pos, 'D')
            current_num += 1
            spiral[current_num] = current_pos

        # Move right width-1
        for y in range(width - 1):
            current_pos = move(current_pos, 'R')
            current_num += 1
            spiral[current_num] = current_pos

    return spiral


def find_taxicab_distance(x):
    """Find distance from x to (0,0) in taxicab geometry"""
    rings_no = which_ring(x)
    spiral = generate_spiral(rings_no)
    pos = spiral[x]
    a, b = pos
    distance = abs(a) + abs(b)
    return distance


# PART 1 SOLUTION
print(find_taxicab_distance(289326))


def generate_sum_spiral(rings):
    """ How many rings the spiral should have"""

    current_num = 1
    current_pos = (0, 0)
    spiral = {current_pos: current_num}

    if rings == 1:
        return spiral

    # Only go on if more than one ring
    for x in range(2, rings + 1):
        width = x * 2 - 1

        # move right 1
        current_pos = move(current_pos, "R")

        j, k = current_pos
        current_num = 0
        for i in spiral:
            a, b = i

            if (not (a == j and b == k)) and (-2 < a - j < 2) and (-2 < b - k < 2):
                current_num += spiral[i]

        spiral[current_pos] = current_num

        # Move up width-2
        for y in range(width - 2):
            current_pos = move(current_pos, 'U')

            j, k = current_pos
            current_num = 0
            for i in spiral:
                a, b = i

                if (not (a == j and b == k)) and (-2 < a - j < 2) and (-2 < b - k < 2):
                    current_num += spiral[i]

            spiral[current_pos] = current_num

        # Move left width-1
        for y in range(width - 1):
            current_pos = move(current_pos, 'L')

            j, k = current_pos
            current_num = 0
            for i in spiral:
                a, b = i

                if (not (a == j and b == k)) and (-2 < a - j < 2) and (-2 < b - k < 2):
                    current_num += spiral[i]

            spiral[current_pos] = current_num

        # Move down width-1
        for y in range(width - 1):
            current_pos = move(current_pos, 'D')

            j, k = current_pos
            current_num = 0
            for i in spiral:
                a, b = i

                if (not (a == j and b == k)) and (-2 < a - j < 2) and (-2 < b - k < 2):
                    current_num += spiral[i]

            spiral[current_pos] = current_num

        # Move right width-1
        for y in range(width - 1):
            current_pos = move(current_pos, 'R')

            j, k = current_pos
            current_num = 0
            for i in spiral:
                a, b = i

                if (not (a == j and b == k)) and (-2 < a - j < 2) and (-2 < b - k < 2):
                    current_num += spiral[i]

            spiral[current_pos] = current_num

    return spiral

new_spiral = generate_sum_spiral(5)

for x in new_spiral:
    print(new_spiral[x], ":", x)
