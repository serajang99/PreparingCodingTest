import sys
input = sys.stdin.readline

# 반복 횟수 n
n = int(input())

for i in range(n):
    ps = input()  # parenthesis string
    s = []  # stack

    for p in ps:
        # '('일 경우 stack에 쌓는다.
        if p == '(':
            s.append(p)

        # ')'일 경우,
        # stack에 남은 '('이 있을 경우 valid이기 때문에 pop해준다.
        # stack이 비워져 있을 경우 NO를 return해야 하는데,
        # for문 밖의 NO의 조건이 stack의 길이가 0이 아닌 것이기 때문에 ')' 를 넣고 break를 걸어준다.
        elif p == ')':
            if len(s) != 0:
                s.pop()
            else:
                s.append(p)
                break
    # stack이 비워져 있을 경우 모든 문자열이 맞게 열고(push) 닫힌(pop) 것이기 때문에 YES를 프린트한다.
    # 그 외에 경우 NO를 프린트한다.
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
