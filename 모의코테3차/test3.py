import math
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    p = [[] for _ in range(n)]
    for i in range(n):
        p[i] = list(map(int, input().rstrip().split()))

    # print(p)

    result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                l1 = math.sqrt((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)
                l2 = math.sqrt((p[i][0]-p[k][0])**2 + (p[i][1]-p[k][1])**2)
                l3 = math.sqrt((p[k][0]-p[j][0])**2 + (p[k][1]-p[j][1])**2)

                lines = sorted([l1, l2, l3])
                # print('-'*10)
                # print(p[i], p[j], p[k])
                # print(lines)
                # print(lines[0]+lines[1], lines[2])
                if lines[0] + lines[1] > lines[2] + 1e-10:
                    result += 1

    print(result)


if __name__ == "__main__":
    main()
