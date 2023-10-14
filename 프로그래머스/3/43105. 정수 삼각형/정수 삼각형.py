def solution(triangle):
    answer = 0
    n = len(triangle)
    floors = [[] for _ in range(n)]
    floors[n-1] = triangle[n-1].copy()
    # print(floors)
    for floor in range(n-1, -1, -1):
        # print("floor: ",floor)
        for x in range(floor):
            # print("index: ",x)
            floors[floor-1].append(triangle[floor-1][x] + max(floors[floor][x], floors[floor][x+1]))
        # print(floors)
    answer = floors[0][0]
    return answer