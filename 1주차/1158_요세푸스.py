# 입력
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

q = []  # 미리 담아놓고 빼올 리스트
result = []  # 결과 리스트

# q에 미리 n만큼의 숫자를 담아놓는다.
# ex) if n=7, q=[1,2,3,4,5,6,7]
for i in range(1, n+1):
    q.append(i)

# num에는 q에서 빼내올 index를 담아준다.
# index는 0부터 시작하기 때문에 k-1을 먼저 담아준다.
num = k-1

# q의 길이가 0이상 일때, 반복한다.
while len(q) > 0:
    # result에 q에서 pop한 값을 순서대로 넣는다.
    result.append(str(q.pop(num)))

    # q의 길이가 0이 되면 반복문을 종료한다.
    # 이후 division by zero를 피하기 위해서도 사용한다.
    if len(q) == 0:
        break

    # pop을 할 경우, 한 자리씩 땡겨지므로 index의 간격은 k-1과 같다.
    num += k-1

    # 만약 num이 q의 index를 벗어날 경우 나머지 값으로 대체한다.
    if num > len(q)-1:
        num %= len(q)

# 출력
print('<', ', '.join(result), '>', sep='')
