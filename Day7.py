def find_root(file):
    sample_file = open(file, 'r')
    sample = []

    while True:
        line = sample_file.readline().strip()
        if '->' in line:
            sample.append(line)
        if line == '':
            break

    roots = []
    leaves = []

    for item in sample:
        x, y = item.split('->')
        x = x.split(' (')[0]
        roots.append(x)
        leaf = y.split(', ')
        for a in leaf:
            leaves.append(a.strip())

    for root in roots:
        if root not in leaves:
            return root

    sample_file.close()
