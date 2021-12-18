import sys
import math
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().strip().split())))

zerolike = math.inf
start, end = 0, n-1

while start < end:
    start_liquid = liquids[start]
    end_liquid = liquids[end]
    c_val = start_liquid + end_liquid

    if zerolike > abs(c_val):
        zerolike = abs(c_val)
        result_start = start_liquid
        result_end = end_liquid

    #print(start, end, start_liquid, end_liquid, c_val, zerolike)
    if c_val <= 0:
        start = start + 1
    else:
        end = end - 1

print(result_start, result_end)
