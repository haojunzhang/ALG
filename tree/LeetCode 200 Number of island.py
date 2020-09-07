"""
1=陸地, 0=水, 數有幾座島
11110
11010
11000
00000
Output : 1

11000
11000
00100
00011
Output : 3

思路
以DFS找, 將拜訪過的標記為2, 避掉0,2


回圈i
    回圈j
        if A[i][j] == 1:
            開始找且標記, 且結果+1
"""


def sub_solve(A, i, j):
    # 原地
    A[i][j] = 2

    # 上
    if i - 1 >= 0 and A[i - 1][j] == 1:  # 注意上邊界
        sub_solve(A, i - 1, j)

    # 下
    if i + 1 < len(A) and A[i + 1][j] == 1:  # 注意下邊界
        sub_solve(A, i + 1, j)

    # 左
    if j - 1 >= 0 and A[i][j - 1] == 1:  # 注意左邊界
        sub_solve(A, i, j - 1)

    # 右
    if j + 1 < len(A[i]) and A[i][j + 1] == 1:  # 注意右邊界
        sub_solve(A, i, j + 1)


def solve(A):
    ret = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 1:
                ret += 1
                sub_solve(A, i, j)  # 標記
    return ret


if __name__ == "__main__":
    print(solve([
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]))  # 1

    print(solve([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]))  # 3

    print(solve([
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
    ]))  # 5
