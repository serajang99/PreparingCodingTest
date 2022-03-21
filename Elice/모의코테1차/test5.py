def main():
    import sys
    input = sys.stdin.readline
    n = int(input().strip())
    lst = list(map(int, input().strip().split()))
    cnt = 0
    for i in range(n):
        indexMin = i
        for j in range(i+1, n):
            if lst[j] < lst[indexMin]:
                indexMin = j
                cnt += 1
                lst[i:j+1] = lst[j:i-1:-1]
                lst[i+1:j+1] = lst[j:i:-1]

    print(cnt)


if __name__ == "__main__":
    main()
