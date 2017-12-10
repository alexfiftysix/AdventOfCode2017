class TreeNode:
    """
    This lil' guy makes a tree node.
    Can add all the weight of the trees above it to determine its weight, does so a lil' recursively
    """

    def __init__(self, weight, parent=None):
        self.weight = weight
        self.parent = parent
        self.child_1 = None
        self.child_2 = None
        self.child_3 = None
        self.children_weight = None
        self.total_weight = None

    def __str__(self):
        if self.child_1:
            return '(' + str(self.weight) + ') [' + self.child_1 + ', ' + self.child_2 + ', ' + self.child_3 + ']'
        else:
            return '(' + str(self.weight) + ') [no children]'

    def generate_total_weight(self):
        if self.child_1 and self.child_2 and self.child_3:
            weight_1 = self.child_1.generate_total_weight()
            weight_2 = self.child_2.generate_total_weight()
            weight_3 = self.child_3.generate_total_weight()
            self.total_weight = weight_1 + weight_2 + weight_3 + self.weight
        else:
            self.total_weight = self.weight

        return self.total_weight

    def get_total_weight(self):
        self.generate_total_weight()
        return self.total_weight

    def get_weight(self):
        return self.weight

    def get_childrens_weight(self):
        return self.children_weight

    def get_children(self):
        return [self.child_1, self.child_2, self.child_3]

    def set_parent(self, parent):
        self.parent = parent

    def set_child_1(self, child):
        self.child_1 = child

    def set_child_2(self, child):
        self.child_2 = child

    def set_child_3(self, child):
        self.child_3 = child

    def generate_children_weight(self):
        weight_1 = self.child_1.get_weight()
        weight_2 = self.child_2.get_weight()
        weight_3 = self.child_3.get_weight()

        self.children_weight = weight_1 + weight_2 + weight_3

    def has_parent(self):
        if self.parent:
            return True
        else:
            return False


def test_tree():
    """
    Tests the tree class generate weight function.
    Returns true if it still works
    """
    base = TreeNode(55)

    first = TreeNode(12, base)
    base.set_child_1(first)

    second = TreeNode(13, base)
    base.set_child_2(second)

    third = TreeNode(15, base)
    base.set_child_3(third)

    a = TreeNode(20, first)
    first.set_child_1(a)

    b = TreeNode(30, first)
    first.set_child_2(b)

    c = TreeNode(40, first)
    first.set_child_3(c)

    # print(base.get_total_weight())
    # print(a.weight + b.weight + c.weight + first.weight + second.weight + third.weight + base.weight)
    print(
        a.weight + b.weight + c.weight + first.weight + second.weight + third.weight + base.weight == base.get_total_weight())


def find_between_brackets(s):
    first = s.index('(')
    second = s.index(')')
    return s[first + 1:second]


def find_root(tree_dict):
    """tree_dict<name: node>"""
    for node in tree_dict:
        print(node, tree_dict[node], tree_dict[node].has_parent())


# Functions above the line
########################################################################################################################
# Scripting below


file_name = "day7_sample.txt"
file = open(file_name, 'r')
stack = file.read()
file.close()

stack = stack.strip()
stack = stack.split('\n')

tree = {}

leaves = []
needs_another_pass = True

print(len(stack))

# move leaf nodes into new list
new_stack = stack[:]
for line in stack:
    if len(line.split()) < 3:
        leaves.append(line)
        new_stack.remove(line)
stack = new_stack

# To start, add all the leaves
for leaf in leaves:
    weight = int(find_between_brackets(leaf))
    name = leaf.split()[0]
    tree[name] = TreeNode(weight)

# first pass adding parents to current leaf nodes
while len(stack) > 0:
    new_stack = stack[:]
    for line in stack:
        line_list = line.split()
        name = line_list[0]
        weight = line_list[1][1:-1]
        children = list()
        children.append(line_list[3][:-1])
        children.append(line_list[4][:-1])
        children.append(line_list[5])
        if children[0] in tree and children[1] in tree and children[2] in tree:
            tree[name] = TreeNode(name, weight)
            tree[children[0]].set_parent(name)
            tree[name].set_child_1(tree[children[0]])
            tree[name].set_child_2(tree[children[1]])
            tree[name].set_child_3(tree[children[2]])

            new_stack.remove(line)
    stack = new_stack

for x in tree:
    print(x, tree[x], tree[x].has_parent())
