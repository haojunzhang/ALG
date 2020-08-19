"""
找出股價利益最大值, 不限買賣次數, 可當日賣完又買
"""


def solve(A):
    ret = 0
    min_value = 9999
    for i in range(1, len(A)):
        ret += max(A[i] - A[i-1], 0)
    return ret


if __name__ == '__main__':
    print(solve([7, 1, 5, 3, 6, 4]))  # 4 + 3 = 7
    print(solve([7, 6, 4, 3, 1]))  # 0
    print(solve([10, 9, 11, 8, 12, 17]))  # 2 + 4 + 5 = 11
    print(solve([9, 5, 4, 1, 3]))  # 2
