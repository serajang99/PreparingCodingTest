import sys
from collections import defaultdict

tree = defaultdict(int)
cnt = 0

for line in sys.stdin:
    a = line.rstrip()
    tree[a] += 1
    cnt += 1

treelist = sorted(tree.items())

for i in range(len(treelist)):
    print("%s %.4f" % (treelist[i][0], treelist[i][1]/cnt*100))
