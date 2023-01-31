from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
nums2i = {}

for i in nums:
    if i in nums2i:
        nums2i[i] += 1
    else:
        nums2i[i] = 1

for i in nums2:
    if i in nums2i:
        print(nums2i[i], end=' ')
    else:
        print(0, end=' ')
