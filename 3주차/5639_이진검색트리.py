import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def get_post(start, end):

    if start > end:
        return

    mid = end + 1
    for i in range(start+1, end+1):
        if preorder[i] > preorder[start]:
            mid = i
            break

    get_post(start+1, mid-1)
    get_post(mid, end)
    print(preorder[start])


preorder = []

while 1:
    try:
        preorder.append(int(input()))
    except:
        break

# 문자열인 경우는 이렇게 input()이면 공백도 문자처리가 돼서 try except 구문에 안걸린다.
# int()의 경우 공백이 int변환이 불가능 하기 때문에 try except 구문에 걸려서 가능하다.

# 문자열 무한 입력 같은 경우 이렇게 받자
# while True:
#   if not input():
#       break
#   else:
#       preorder.append(input())

get_post(0, len(preorder)-1)
