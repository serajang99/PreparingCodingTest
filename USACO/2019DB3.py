with open("lineup.in", "r") as fin:
    n = int(fin.readline())
    constraints = [list(line.split()) for line in fin]

print(constraints, n)
new_constraints = []
for constraint in constraints:
    new_constraints.append([constraint[0], constraint[-1]])

print(new_constraints, n)

cows = ["Bessie", "Buttercup", "Belinda",
        "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
cows = sorted(cows)

cows_dict = {}
cnt = 0
for cow in cows:
    cows_dict[cow] = cnt
    cnt += 1

print(cows_dict)


result = 0
with open("lineup.out", "w+") as fout:
    print(result, file=fout)
