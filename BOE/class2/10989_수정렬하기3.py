import sys
input = sys.stdin.readline

n = int(input())
nums = {}
for i in range(n):
    num = int(input())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

for key, val in sorted(nums.items(), key=lambda x: x[0]):
    for _ in range(val):
        print(key)
