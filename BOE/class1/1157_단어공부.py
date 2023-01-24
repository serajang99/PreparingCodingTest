from collections import defaultdict
import sys
input = sys.stdin.readline

word = input().rstrip().upper()
worddict = defaultdict(int)

for w in word:
    worddict[w] += 1

sorteddict = sorted(worddict.items(), key=lambda x: x[1], reverse=True)
if len(sorteddict) == 1 or sorteddict[0][1] != sorteddict[1][1]:
    print(sorteddict[0][0])
else:
    print("?")
