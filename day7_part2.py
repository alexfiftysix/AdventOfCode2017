# from anytree import Node, RenderTree
from Day7 import find_root

text_file = 'day7_sample.txt'

root = find_root(text_file)

sample_file = open(text_file, 'r')
stack = []

# Get everything from the file to the stack
while True:
    line = sample_file.readline().strip()
    if line == '':
        break
    stack.append(line)

sample_file.close()

# Get the weight of everything
weights = {}

for process in stack:
    process = process.split()
    x = process[0]
    y = process[1].strip('(').strip(')')
    weights[x] = int(y)

# Weights gotten

# Put leafs in dictionary
fake_tree = {}
for x in stack:
    if '->' in x:
        line = x.split()
        line = [x.strip(',') for x in line]
        fake_tree[line[0]] = line[3:]


for x in fake_tree:
    print(x, ":", fake_tree[x])
    print(weights[x], ":", [weights[i] for i in fake_tree[x]])
    print(sum([weights[i] for i in fake_tree[x]], weights[x]))
    print()
