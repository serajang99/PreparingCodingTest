import sys
input = sys.stdin.readline

with open("whereami.in", "r") as fin:
    n = int(fin.readline())
    mailboxes = list(fin.readline().rstrip())

result = 1
flag = 0
for k in range(1, n+1):  # k : mailbox 길이
    flag = 0
    i = 0
    while(i+k <= n):
        for j in range(0, i):
            if mailboxes[i:i+k] == mailboxes[j:j+k]:
                flag = 1
        i += 1
    if flag == 0:
        result = k
        break


with open("whereami.out", "w+") as fout:
    print(result, file=fout)
