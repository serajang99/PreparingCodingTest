from itertools import combinations, permutations, product

def solution(word):
    answer = 0
    aeiou = ['A', 'E', 'I', 'O', 'U']
    li = []
    for i in range(1, 6):
        for j in product(aeiou, repeat=i):
            li.append("".join(j))
    li.sort()
    answer = li.index(word) + 1
    return answer