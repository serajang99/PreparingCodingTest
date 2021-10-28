import sys
import heapq
input = sys.stdin.readline

t = int(input())  # 테스트케이스
for i in range(t):
    minheap = []  # 최소 힙
    maxheap = []  # 최대 힙
    n = int(input())  # 연산 수
    visit = [False] * n  # 연산 수만큼 visit 리스트를 생성하고 False로 초기화한다.
    for j in range(n):  # j: 연산 순서
        command = input().rstrip().split()
        # Insert
        # heapq는 최소힙이 기본이기 때문에 (튜플) 형태로 (Insert할 정수, 현재 연산 순서)를 넣는다.
        # 최대힙을 구현하기 위해서는 음수로 값을 바꿔서 넣어줘야한다.
        # 현재 연산 순서의 visit값을 true로 변경한다.
        if command[0] == 'I':
            heapq.heappush(minheap, (int(command[1]), j))
            heapq.heappush(maxheap, (-int(command[1]), j))
            visit[j] = True

        # Delete
        # -1의 경우 minheap에서 빼는 연산을 해줘야한다.
        # 이때, visit가 false인 값들도 minheap의 앞부분에 남아있을 수 있기 때문에(ex. maxheap에서 visit가 False로 설정되었으나 minheap에서 heappop되지 않은 경우) 그 부분을 제거해준다.
        # 즉, minheap에서 visit가 true인 가장 작은 값을 찾아
        # visit를 False로 바꾸고, heappop하는 과정을 통해 delete한다.
        # 1의 경우에는 maxheap에서 위의 과정이 반복된다.
        elif command[0] == 'D':
            if command[1] == '-1':
                while minheap and not visit[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    visit[minheap[0][1]] = False
                    heapq.heappop(minheap)
            elif command[1] == '1':
                while maxheap and not visit[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    visit[maxheap[0][1]] = False
                    heapq.heappop(maxheap)

    # Delete 연산과 마찬가지로 visit가 true인 heap의 가장 높은 값을 찾는다.
    while minheap and not visit[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visit[maxheap[0][1]]:
        heapq.heappop(maxheap)

    # 출력
    if len(minheap) == 0:
        print('EMPTY')
    else:
        print(-maxheap[0][0], minheap[0][0])

# 첫번째 구현 방법
# heapq를 이용해 minheap만 구현 후, 최솟값을 빼는 것은 remove로 구현했으나 시간초과,,
# t = int(input())
# for i in range(t):
#     minheap = []
#     n = int(input())
#     for j in range(n):
#         command = input().rstrip().split()
#         if command[0] == 'I':
#             heapq.heappush(minheap, int(command[1]))
#         elif command[0] == 'D':
#             if len(minheap) == 0:
#                 continue
#             if command[1] == '-1':
#                 heapq.heappop(minheap)
#             elif command[1] == '1':
#                 minheap.remove(min(minheap))
#         # print(heap)
#     if len(minheap) == 0:
#         print('EMPTY')
#     else:
#         print(minheap[-1], minheap[0])
'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''
