import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    nums = list(map(int, input().rstrip().split()))  # 한줄씩 입력받아 한 숫자씩 읽어들이기 위함
    for num in nums:
        heapq.heappush(heap, (num))
        # maxheap을 써야하나 했지만 maxheap에서 heappop은 최댓값을 pop하는 것이고,
        # 여기서 최솟값을 pop하기 어려우므로, heap의 크기를 n**2로 만들어주는 수 밖에 없다. -> 메모리초과 or 구현은 가능하나 시간초과(remove 등)
        # 따라서, minheap을 쓰면서 heap의 크기를 n으로 유지시켜주는 것이 포인트이다.
        if len(heap) > n:
            heapq.heappop(heap)

print(min(heap))

'''
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
'''
