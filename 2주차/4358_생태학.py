import sys
from collections import defaultdict

# defaultdict는 dict에 초기값을 설정해줄 수 있다.
# int를 사용하면 0으로 초기화되며, lambda식을 통해 초기값을 설정해 줄 수 도 있다.
# 여기서는 개체 수를 의미하므로 int로 설정하여 초기값을 0으로 설정해준다.
tree = defaultdict(int)
cnt = 0  # 총 개체 수

for line in sys.stdin:
    a = line.rstrip()
    tree[a] += 1
    cnt += 1

treelist = sorted(tree.items())  # dict를 key순으로 정렬할 때 쓰기 좋은 방법이다.

for i in range(len(treelist)):
    print("%s %.4f" % (treelist[i][0], treelist[i][1]/cnt*100))
    # round(,4)를 쓰는 출력을 했다가 틀린 값이 나왔다. 안전하게 formatting을 쓰는 것이 좋겠다.
