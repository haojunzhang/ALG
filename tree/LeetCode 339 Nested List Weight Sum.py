"""
加總權重

1.
[[1,1],2,[1,1]]
4個1在第2層 4 x 2 = 8
1個2在第1層 2 x 1 = 2
結果 = 10

2.
[1,[4,[6]]]
1 x 1 =  1
4 x 2 =  8
6 x 3 = 18
結果 = 27

思路
回圈
    ret += 如是list則遞迴
    ret += 如是int則回傳該值
ret
"""


def solve(data):
    return dfs(data, 0)


def dfs(data, level):
    if isinstance(data, int):
        return data * level

    if isinstance(data, list):
        ret = 0
        for val in data:
            ret += dfs(val, level + 1)
        return ret


if __name__ == "__main__":
    print(solve([[1, 1], 2, [1, 1]]))
    print(solve([1, [4, [6]]]))
