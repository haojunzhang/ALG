"""
加總權重
與339相反, 愈下面權重愈低
1.
[[1,1],2,[1,1]]
(2 x 2) + (1 x 4) = 8

2.
[1,[4,[6]]]
(3 x 1) + (2 x 4) + (1 x 6) = 17

思路
與339類似, 再用1個dict存該層的值, 如下
以1.為例
m[1] = 2
m[2] = 1 + 1 + 1 + 1 = 4

ret = 0
for k, v in m.items():
    weight = len(m) - k + 1
    ret += weight * v
ret
"""


def solve(data):
    m = {}
    dfs(data, 0, m)
    ret = 0
    for k, v in m.items():
        weight = len(m) - k + 1
        ret += weight * v
    return ret


def dfs(data, level, m):
    if level != 0 and level not in m:
        m[level] = 0

    if isinstance(data, int):
        m[level] += data

    if isinstance(data, list):
        for val in data:
            dfs(val, level + 1, m)


if __name__ == "__main__":
    print(solve([[1, 1], 2, [1, 1]]))
    print(solve([1, [4, [6]]]))
