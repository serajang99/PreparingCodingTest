def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks = sorted(rocks)

    while start <= end:
        mid = (start+end)//2
        cur, delete = 0, 0
        for rock in rocks:
            if rock-cur < mid:
                delete += 1
            else:
                cur = rock
        if distance-cur < mid:
            delete += 1

        if delete > n:
            end = mid-1
        else:
            start = mid+1
            answer = mid

    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
