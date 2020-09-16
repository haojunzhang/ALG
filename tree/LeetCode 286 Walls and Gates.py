"""
求出所有房間到門最近的步數

-1 = 牆
0 = 門
INF = 房間

before
INF   -1    0  INF
INF  INF  INF   -1
INF   -1  INF   -1
  0   -1  INF  INF

after
  3   -1    0    1
  2    2    1   -1
  1   -1    2   -1
  0   -1    3    4

思路
先找出0, 開始dfs下去
跳過
  1.碰牆壁
  2.越界 
  3.當下值比該位置值大(挑最近所以取小值)跳過
"""


def solve(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                dfs(data, i, j, 0)


def dfs(data, i, j, val):
    if i < 0 or i >= len(data):
        return

    if j < 0 or j >= len(data[i]):
        return

    if data[i][j] < val:
        return

    data[i][j] = val
    dfs(data, i - 1, j, val + 1)
    dfs(data, i + 1, j, val + 1)
    dfs(data, i, j - 1, val + 1)
    dfs(data, i, j + 1, val + 1)


if __name__ == "__main__":
    data = [
        [999, -1, 0, 999],
        [999, 999, 999, -1],
        [999, -1, 999, -1],
        [0, -1, 999, 999]
    ]

    solve(data)

    for row in data:
        print(row)
