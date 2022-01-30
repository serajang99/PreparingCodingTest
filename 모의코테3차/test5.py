import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))  # n개 재료 각각 개수
    b = [[] for _ in range(m)]  # m개의 레시피 []
    for i in range(m):
        b[i] = list(map(int, input().rstrip().split()))  # n개 재료 각 개수 + 금액

    print(b[0][-1])


if __name__ == "__main__":
    main()
