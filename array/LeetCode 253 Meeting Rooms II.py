"""
給多個會議時間區間, 回傳需要幾間會議室

1.
Input: [[0,30],[5,10],[15,20]]
Output: 2

2.
Input: [[7,10],[2,4]]
Output: 1

思路
1.
利用key sorted map
 0 :  1          0 :  1
30 : -1          5 :  1
 5 :  1   >>>   10 : -1
10 : -1         15 :  1
15 :  1         20 : -1
20 : -1         30 : -1
回圈map:
    變數rooms = 同時使用的數量
    ret = 結果(取最大值)

2.
建兩個array, 分別放起始值與終止值, 並且都排序
ret = 結果最多也就len(A)
end_position = 終止值指標
回圈A
    當下起始值 < 終止值指標值 ret++, 反之end_position++
0
|    5
|    |
|   10
|       15
|       |
|       20
|
30

大概感覺是在end_position的值前起始了幾次
"""


def solve1(A):
    m = {}
    for it in A:
        if it[0] not in m:
            m[it[0]] = 0
        m[it[0]] += 1

        if it[1] not in m:
            m[it[1]] = 0
        m[it[1]] -= 1

    ret = 0
    using_rooms = 0
    for k in sorted(m.keys()):
        v = m[k]
        using_rooms += v
        ret = max(ret, using_rooms)

    return ret


def solve2(A):
    starts = []
    ends = []
    for it in A:
        starts.append(it[0])
        ends.append(it[1])
    starts.sort()
    ends.sort()

    ret = 0
    end_position = 0

    for i in range(len(A)):
        if starts[i] < ends[end_position]:
            ret += 1
        else:
            end_position += 1

    return ret


if __name__ == "__main__":
    # print(solve1([[0, 30], [5, 10], [15, 20]]))  # 2
    # print(solve1([[7, 10], [2, 4]]))  # 1
    # print(solve1([[0, 15], [5, 20], [10, 25], [14, 35]]))  # 4

    print(solve2([[0, 30], [5, 10], [15, 20]]))  # 2
    print(solve2([[7, 10], [2, 4]]))  # 1
    print(solve2([[0, 15], [5, 20], [10, 25], [14, 35]]))  # 4
