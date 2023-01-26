import math
import sys
input = sys.stdin.readline


def is_prime(num):
    if num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True


n = int(input())
numbers = list(map(int, input().rstrip().split()))
cnt = 0
for num in numbers:
    prime = is_prime(num)
    if prime:
        cnt += 1
print(cnt)
