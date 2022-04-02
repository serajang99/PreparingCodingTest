from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    time, answer, flag = 0, 0, 0
    d, n, u = map(int, input().rstrip().split())
    delivery = deque([])
    times = deque([])
    for j in range(d):
        m, l, e = map(int, input().rstrip().split())
        delivery.append([m, l, m+e])
        times.append(m)
    real_delivery = deque([])
    orders = deque(list(map(int, input().rstrip().split())))
    times.extend(orders)
    times = deque(sorted(times))

    print(times, delivery, orders, real_delivery)
    while flag == 0 and orders and times:
        time = times.popleft()

        if len(delivery) != 0:
            if time == delivery[0][0]:
                real_delivery.append(delivery.popleft())
                real_delivery = deque(
                    sorted(real_delivery, key=lambda x: x[2]))

        if len(real_delivery) != 0:
            if time == real_delivery[0][2]:
                real_delivery.popleft()

        if time == orders[0]:
            stock = sum(l for _, l, _ in real_delivery)
            print(stock)

            if stock >= u:
                orders.popleft()
                tmp = u
                while tmp > 0:
                    # print("tmp:", tmp)
                    if real_delivery[0][1] > tmp:
                        real_delivery[0][1] -= tmp
                        tmp = 0
                    else:
                        tmp -= real_delivery[0][1]
                        real_delivery.popleft()
                # print(real_delivery)
                answer += 1
            else:
                flag = 1

        print(time, delivery, orders, real_delivery, flag)

    print("Case #%d: %d" % (i+1, answer))
