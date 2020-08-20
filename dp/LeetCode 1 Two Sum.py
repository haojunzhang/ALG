"""
gap:差額
position:位置
target:目標
判斷gap是否有出現過, 有的話回傳
存判斷過的值與該值的位置, value:position

過程:
    arr = [1, 3, 4, 8, 10]
    target = 13
    ======================
    i = 0
    m = {} bf
    arr[i] = 1
    gap = 12
    m = {1: 0} af
    ======================
    i = 1
    m = {1: 0} bf
    arr[i] = 3
    gap = 10
    m = {1: 0, 3: 1} af
    ======================
    i = 2
    m = {1: 0, 3: 1} bf
    arr[i] = 4
    gap = 9
    m = {1: 0, 3: 1, 4: 2} af
    ======================
    i = 3
    m = {1: 0, 3: 1, 4: 2} bf
    arr[i] = 8
    gap = 5
    m = {1: 0, 3: 1, 4: 2, 8: 3} af
    ======================
    i = 4
    m = {1: 0, 3: 1, 4: 2, 8: 3} bf
    arr[i] = 10
    gap = 3
    gap in m
    return [m[gap], i] # [1, 4]
    ======================
Time complexity : O(N)
Space complexity : O(N)
"""


def two_sum(arr, target):
    m = {}
    for i in range(len(arr)):
        gap = target - arr[i]
        if gap in m:
            return [m[gap], i]

        # 存此值出現在第幾個位置
        m[arr[i]] = i
    return []


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9
    ret = two_sum(arr, target)
    print(ret)  # [0, 1]

    arr = [1, 3, 4, 8, 10]
    target = 13
    ret = two_sum(arr, target)
    print(ret)  # [1, 4]

    arr = [3, 5, 6]
    target = 7
    ret = two_sum(arr, target)
    print(ret)  # []
