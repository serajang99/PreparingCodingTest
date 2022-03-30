from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = [[truck_weights.popleft(), 1]]
    answer = 1
    while bridge:
        if truck_weights:
            cur = truck_weights[0]
        else:
            cur = bridge[0][0]
        summ = 0

        for b in bridge:
            b[1] += 1

        for b in bridge:
            if b[1] > bridge_length:
                bridge.pop(0)
        answer += 1

        for w, c in bridge:
            summ += w

        if summ+cur <= weight:
            if len(bridge) <= bridge_length and truck_weights:
                bridge.append([truck_weights.popleft(), 1])

        if len(truck_weights) == 0 and len(bridge) == 0:
            break

    return answer


# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length, weight, truck_weights))
