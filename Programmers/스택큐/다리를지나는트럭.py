from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([truck_weights.popleft()])
    while bridge:
        cur = truck_weights[0]
        if sum(bridge)+cur <= weight and len(bridge) <= bridge_length and truck_weights:
            bridge.append(truck_weights.popleft())

        if len(bridge) > bridge_length:
            bridge.popleft()

        answer += 1
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
