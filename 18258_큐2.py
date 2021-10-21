import sys
input = sys.stdin.readline

n = int(input())
q = []  # queue
cnt = 0  # queue에서 front index를 가리킨다.

for i in range(n):
    # command(cmd)를 list로 받는다.
    cmd = input().rstrip().split()

    # push 연산
    if cmd[0] == 'push':
        q.append(cmd[1])

    # pop 연산
    # cnt를 올려주는 것으로 front index를 하나 높여 pop을 대신한다.
    elif cmd[0] == 'pop':
        if cnt < len(q):
            print(q[cnt])
            cnt += 1
        else:
            print(-1)

    # front 연산
    elif cmd[0] == 'front':
        if cnt < len(q):
            print(q[cnt])
        else:
            print(-1)

    # back 연산
    elif cmd[0] == 'back':
        if cnt < len(q):
            print(q[-1])
        else:
            print(-1)

    # size 연산
    elif cmd[0] == 'size':
        if cnt <= len(q):
            print(len(q)-cnt)

    # empty 연산
    elif cmd[0] == 'empty':
        if cnt == len(q):
            print(1)
        else:
            print(0)

# 시간초과가 나서 자꾸 애먹었다.
# queue의 경우, pop연산에서 맨앞 원소를 빼주고 땡기는 과정이 시간을 많이 잡아먹는다.
# 따라서 .pop()을 쓰지 않고 cnt에 queue의 front index를 담아 해결하는 방법이 있다.
# 다른 방법으로는 collections의 deque(덱)을 사용하는 방법이 있다.
# 이는 18258_큐2_deq.py에서 다룰 예정이다.
