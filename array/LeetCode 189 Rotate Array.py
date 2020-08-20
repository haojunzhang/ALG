"""
滾動陣列裡的值
如[1, 2, 3, 4, 5], 2表示往右邊滾兩次
[1, 2, 3, 4, 5]
[5, 1, 2, 3, 4]
[4, 5, 1, 2, 3]

公式
整個reverse後
第兩個集合在reverse
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1] 整體reverse
['5, 4', '3, 2, 1'] 兩個集合在個別reverse
['4, 5', '1, 2, 3']
[4, 5, 1, 2, 3]
"""


def solve(A, n):
    A.reverse()

    a = A[:n]
    a.reverse()

    b = A[n:]
    b.reverse()
    return a + b


if __name__ == "__main__":
    print(solve([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
