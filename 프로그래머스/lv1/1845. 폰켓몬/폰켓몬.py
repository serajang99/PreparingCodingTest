def solution(nums):
    answer = 0
    nums_set = set(nums)
    N = len(nums)//2
    if len(nums_set) <= N:
        answer = len(nums_set)
    else:
        answer = N
    return answer