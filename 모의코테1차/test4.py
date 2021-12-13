def get_dist_sum(houses, n):
    left, right, dist = 0, 0, 0
    for house in houses:
        if house < n:
            left += house-n
        else:
            right += house-n
        dist += abs(house-n)
    return abs(left), right, dist


def main():

    import math
    n = input()
    houses = list(map(int, input().strip().split()))
    houses = sorted(houses)

    start = houses[0]
    end = houses[-1]
    mid = (start+end)//2

    min_office = math.inf
    offices = []
    cnt = 0

    while start < end:
        left, right, dist = get_dist_sum(houses, mid)
        if min_office > dist:
            cnt = 0
            min_office = dist
            offices = [mid]
        elif min_office == dist:
            cnt += 1
            offices.append(mid)

        if left < right:
            start = mid+1
        else:
            end = mid-1
        mid = (start+end)//2

    if len(offices) == 1:
        print(1)
    elif len(offices) == 2:
        print(abs(offices[1]-offices[0]))


if __name__ == "__main__":
    main()
