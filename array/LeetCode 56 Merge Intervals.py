"""
合併重疊的區段
input = [[1, 3], [2, 6], [8, 10], [15, 18]]
output = [[1, 6], [8, 10], [15, 18]]

思路
先排序
這樣只有下面3種狀況
1.
[  A  ]
  [  B  ]
2.
[   A   ]
  [ B ]
3.
[ A ] [ B ]

新區段 = (A.start, max(A.end, B.end))
"""


def solve(data):
    arr = sorted(data)
    ret = [data[0]]

    for it in arr[1:]:
        if ret[-1][0] <= it[0] and it[0] <= ret[-1][1]:
            # 重疊
            ret[-1][1] = max(ret[-1][1], it[1])
        else:
            ret.append(it)

    return ret


if __name__ == "__main__":
    # [[1, 6], [8, 10], [15, 18]]
    print(solve([[1, 3], [2, 6], [8, 10], [15, 18]]))

    # [[1, 5]]
    print(solve([[1, 4], [4, 5]]))
