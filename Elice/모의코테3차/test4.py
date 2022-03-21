import math
import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().rstrip().split())
    prices = list(map(int, input().rstrip().split()))

    if n > m:
        print(-1)
    else:
        for _ in range(m-n):
            min_sum, min_j = math.inf, 0
            for j in range(0, len(prices)-1):
                if min_sum >= prices[j]+prices[j+1]:
                    min_j = j
                    min_sum = prices[j]+prices[j+1]
            # print(min_sum, min_j)
            new_prices = []
            for j in range(0, min_j):
                new_prices.append(prices[j])
            new_prices.append(min_sum)
            for j in range(min_j+2, len(prices)):
                new_prices.append(prices[j])
            prices = new_prices
            print(prices)

        print(min(prices))


if __name__ == "__main__":
    main()
