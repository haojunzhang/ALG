"""
給多個會議時間區間, 如都可參加回傳True, 反之False

1.
Input: [[0,30],[5,10],[15,20]]
Output: False

2.
Input: [[7,10],[2,4]]
Output: True

思路
1.簡單暴力兩倆互相比對a, b, 如a[0] <= b[0] and b[0] <= a[1] 代表overlap, return False
    比完後將a, b互換(不然下面這種情況會漏)
    a = [4, 6]
    b = [1, 10]

2.先排序, 從i = 1開始往前一個比
    如i的起始值小於i-1的終止值代表有overlap
"""


def solve1(A):
    for i in range(len(A)-1):
        for j in range(i + 1, len(A)):
            if A[i][0] <= A[j][0] and A[j][0] <= A[i][1] or \
                    A[j][0] <= A[i][0] and A[i][0] <= A[j][1]:
                return False
    return True


def solve2(A):
    B = sorted(A, key=lambda it: it[0])
    for i in range(1, len(B)):
        if B[i-1][0] <= B[i][0] and B[i][0] <= B[i-1][1]:
            return False
    return True


if __name__ == "__main__":
    # print(solve1([[0, 30], [5, 10], [15, 20]]))  # False
    # print(solve1([[0, 30], [15, 35], [35, 50]]))  # False
    # print(solve1([[0, 30], [31, 50], [51, 59]]))  # True
    # print(solve1([[7, 10], [2, 4]]))  # True

    print(solve2([[0, 30], [5, 10], [15, 20]]))  # False
    print(solve2([[0, 30], [15, 35], [35, 50]]))  # False
    print(solve2([[0, 30], [31, 50], [51, 59]]))  # True
    print(solve2([[7, 10], [2, 4]]))  # True
