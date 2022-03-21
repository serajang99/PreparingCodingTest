def main():
    n, m = map(int, input().strip().split())
    pMap = [[] for _ in range(n)]
    for i in range(n):
        pMap[i] = list(map(int, input().strip().split()))

    y, x = map(int, input().strip().split())
    x -= 1
    y -= 1

    di = [(0, 0), (-1, 0), (0, -1), (0, 1), (1, 0)]
    road = [(y, x)]
    while True:

        if (0 > x or x >= m or 0 > y or y >= n):
            print(-1)
            break

        for i in range(1, 5):
            if pMap[y][x] == i:
                y += di[i][0]
                x += di[i][1]
                break

        cnt = 0
        for i in range(len(road)):
            if road[i] == (y, x):
                print(len(road)-i)
                cnt += 1
                break

        if cnt == 0:
            road.append((y, x))
        else:
            break

        # if len(road) > 1:
        #     road_2 = (road[-2], road[-1])
        #     if road_2 == (3, 2) or road_2 == (1, 4):
        #         print(2)
        #         break
        # if len(road) > 3:
        #     road_4 = (road[-4], road[-3], road[-2], road[-1])
        #     if road_4 == (1, 2, 4, 3) or road_4 == (3, 4, 2, 1):
        #         print(4)
        #         break


if __name__ == "__main__":
    main()
