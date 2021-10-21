import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque([])  # deque

for i in range(n):
    # command(cmd)를 list로 받는다.
    cmd = input().rstrip().split()

    # push 연산
    if cmd[0] == 'push':
        dq.append(cmd[1])

    # pop 연산
    elif cmd[0] == 'pop':
        if len(dq) > 0:
            print(dq.popleft())  # deque는 양방향이기 때문에 popleft()가 가능하다.
        else:
            print(-1)

    # front 연산
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)

    # back 연산
    elif cmd[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)

    # size 연산
    elif cmd[0] == 'size':
        print(len(dq))

    # empty 연산
    elif cmd[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)


# deque란 무엇인가?
    # 양방향큐(Doubly Ended Queue)
# deque는 언제 쓰는가?
    # 스택처럼 사용할 수도 있고, 큐처럼 사용할 수도 있다.
    # 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는데 최적화 되어있다.
    # == O(1)
    # queue의 pop대신 사용하기 좋겠다.
