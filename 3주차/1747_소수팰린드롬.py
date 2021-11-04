import sys
import math
input = sys.stdin.readline


def isPrime(x):  # 소수인지 판별해주는 함수
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def isp(p):
    str_p = str(p)
    if str_p == str_p[::-1]:
        return True
    else:
        return False


n = int(input())
while 1:
    if n == 1:
        n += 1
    if isp(n):
        if isPrime(n):
            print(n)
            break
    n += 1
