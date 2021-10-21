import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dq = deque([i for i in range(1, n+1)])  # 1~n까지의 배열을 deque로 바꿔준다.

# 한턴에 한카드씩 버리므로, n-1번 반복하면 마지막 카드가 남는다.
for i in range(n-1):
    dq.popleft()  # 제일 위의 카드를 버린다.
    temp = dq.popleft()  # 두번째 카드를 temp에 저장해놓는다.
    dq.append(temp)  # 제일 아래 카드 밑으로 옮긴다.

print(dq[0])  # 마지막 카드를 프린트한다.
