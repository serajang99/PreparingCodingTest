import sys
input = sys.stdin.readline


def main():
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    summ = 0
    for i in range(1, n, 2):
        # print(nums[i])
        if nums[i] % 2 == 0:
            summ += nums[i]
    print(summ)


if __name__ == "__main__":
    main()
