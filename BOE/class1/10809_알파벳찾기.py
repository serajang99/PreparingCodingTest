from collections import defaultdict
import sys

input = sys.stdin.readline

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sindex = dict.fromkeys(alphabet, -1)

S = input().rstrip()
for i in range(len(S)):
    if sindex[S[i]] == -1:
        sindex[S[i]] = i

for i in sindex.values():
    print(i, end=' ')
print()
