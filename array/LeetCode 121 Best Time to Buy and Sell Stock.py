"""
找出股價利益最大值, 只買賣一次的話
"""


def solve(A):
    ret = 0
    min_value = 9999
    for i in A:
        if i < min_value:
            min_value = i
        ret = max(ret, i - min_value)
    return ret


if __name__ == '__main__':
    print(solve([7, 1, 5, 3, 6, 4]))  # 5
    print(solve([7, 6, 4, 3, 1]))  # 0
    print(solve([10, 9, 11, 8, 12, 17]))  # 9
    print(solve([9, 5, 4, 1, 3]))  # 2
