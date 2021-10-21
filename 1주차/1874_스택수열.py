import sys
input = sys.stdin.readline
n = int(input())

s = [1]  # stack
# 무조건 한번씩 쓰이는 큐 but pop연산이 필요한게 아니라서 그냥 list를 썼다.
li = [i for i in range(1, n+1)]
cnt = 1  # li의 top
result = ['+']  # 결과값 처음 1 push 값을 default로 한다.
error = 0
# s[-1] is stack top
for i in range(n):
    data = int(input())

    # s[-1]가 index error나는 것을 방지한다.
    if not s:
        s.append(-1)

    # data가 stack의 top보다 작으면 data와 같아질때까지 넣어주고,
    # data와 stack의 top이 같아지면 pop한다.
    if s[-1] <= data:
        for i in range(cnt, data):
            s.append(li[i])
            result.append('+')
            cnt += 1

        if s[-1] == data:
            result.append('-')
            s.pop()

    # error flag를 세우고 break를 걸어준다.
    elif s[-1] > data:
        error = 1
        break

# 출력
if error:
    print("NO")
else:
    for i in result:
        print(i)
