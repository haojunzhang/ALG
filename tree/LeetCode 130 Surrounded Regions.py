"""
類似圍棋, 但有摸到邊界不算

before
X X X X
X O O X
X X O X
X O X X

after
X X X X
X X X X
X X X X
X O X X

思路
先把邊界的O代替成另一個值(例如A), 剩下的就是被圍在中間的
最後再把O改回X, A改回O
"""


def solve(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
                replace_o(data, i, j)

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'O':
                data[i][j] = 'X'
            if data[i][j] == 'A':
                data[i][j] = 'O'


def replace_o(data, i, j):
    if i < 0 or i >= len(data):
        return

    if j < 0 or j >= len(data[i]):
        return

    if data[i][j] == 'O':
        data[i][j] = 'A'

        replace_o(data, i - 1, j)
        replace_o(data, i + 1, j)
        replace_o(data, i, j - 1)
        replace_o(data, i, j + 1)


if __name__ == "__main__":
    # 1.
    data = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]

    solve(data)

    for row in data:
        print(row)
    print('---')
    # 2.
    data = [
        ['O', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'X', 'X'],
    ]

    solve(data)

    for row in data:
        print(row)
    print('---')
    # 3.
    data = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X'],
    ]

    solve(data)

    for row in data:
        print(row)
