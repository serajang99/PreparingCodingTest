import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = {}
pokemon2 = {}
for i in range(n):
    poke = input().rstrip()
    pokemon[i+1] = poke
    pokemon2[poke] = i+1

for _ in range(m):
    poke = input().rstrip()
    if "0" <= poke[0] <= "9":
        poke = int(poke)
        print(pokemon[poke])
    else:
        print(pokemon2[poke])
