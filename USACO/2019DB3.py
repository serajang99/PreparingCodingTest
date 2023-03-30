from itertools import permutations

n = int(input())
constraints = []
cows_dict = {}
for i in range(n):
    li = input().rstrip().split()
    constraints.append((li[0], li[-1]))
    if li[0] not in cows_dict:
        cows_dict[li[0]] = [li[-1]]
    else:
        cows_dict[li[0]].append(li[-1])

    if li[-1] not in cows_dict:
        cows_dict[li[-1]] = [li[0]]
    else:
        cows_dict[li[-1]].append(li[0])

cows = ["Bessie", "Buttercup", "Belinda",
        "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
cows = sorted(cows)

visited = {cow: False for cow in cows}
for cow in permutations(cows, len(cows)):
    flag = 0
    for c in range(0, len(cow)):
        if cow[c] in cows_dict:
            if c == 0:
                if cows_dict[cow[c]] == [cow[c+1]]:
                    continue
                else:
                    flag = 1
                    break
            elif c == len(cow) - 1:
                if cows_dict[cow[c]] == [cow[c-1]]:
                    continue
                else:
                    flag = 1
                    break
            else:
                if cows_dict[cow[c]] == [cow[c-1]] or cows_dict[cow[c]] == [cow[c+1]] or cows_dict[cow[c]] == [cow[c-1], cow[c+1]] or cows_dict[cow[c]] == [cow[c+1], cow[c-1]]:
                    continue
                else:
                    flag = 1
                    break
    if flag == 0:
        break

for c in cow:
    print(c)
