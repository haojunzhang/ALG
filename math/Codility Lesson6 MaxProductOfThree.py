"""
找出3數乘積最大值
[-3, 1, 2, -2, 5, 6]
回傳2 x 5 x 6 = 60

先排序
A[i] x A[i + 1] x A[i + 2] 找最大值
考慮負負得正, 最後要和A[0]xA[1]xA[len-1] 比
"""


def solve(A):
    A.sort()
    max_v = A[0] * A[1] * A[2]
    for i in range(1, len(A)-2):
        max_v = max(A[i] * A[i+1] * A[i+2], max_v)

    return max(max_v, A[0] * A[1] * A[len(A)-1])


if __name__ == "__main__":
    print(solve([-3, 1, 2, -2, 5, 6]))  # 60
    print(solve([-5, -4, -3, -2, -1, 5]))  # 100
    print(solve([1, 2, 3, 4, 5]))  # 60
