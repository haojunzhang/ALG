"""
排序前與後大概分幾分
以下方為例
[2, 4, 1, 6, 5, 9, 7] >>> [1, 2, 4, 5, 6, 7, 9] >>> 3
因為只有[2, 4, 1], [6, 5], [9, 7]三個區塊異動, 回傳3
[4, 3, 2, 6, 1] >>> [1, 2, 3, 4, 6] >>> 1
[2, 1, 6, 4, 3, 7] >>> [1, 2, 3, 4, 6, 7] >>> 3

思路
先得出位置的變化
data = []

[0,1]  # 從位置0移動到位置1
[1,2]  # 從位置1移動到位置2
[2,0]  # 從位置2移動到位置1
從上面3個得出 >> [0,2]

[3,4]  # 從位置3移動到位置4
[4,3]  # 從位置4移動到位置3
從上面2個得出 >> [3,4]
[5,6]  # 從位置5移動到位置6
[6,5]  # 從位置6移動到位置5
從上面2個得出 >> [5,6]
判斷交集的function要確認
如有交集則擴大, 無則ret.append, 最後回傳len(ret)
"""


def solution(A):
    B = A.copy()
    B.sort()
    data = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                data.append([i, j] if j > i else [j, i])
                break
    ret = []
    for it in data:
        if len(ret) == 0:
            ret.append(it.copy())
        else:
            have_union_r = None
            for r in ret:
                print(f'{it} & {r} = {have_union(it, r)}')
                if have_union(it, r):
                    have_union_r = r
                    break
            if have_union_r:
                have_union_r[0] = min(it[0], r[0])
                have_union_r[1] = max(it[1], r[1])
            else:
                ret.append(it.copy())
    return len(ret)


def have_union(A, B):
    # A:[0,2]
    # B:[2,5]
    # return True
    if A[1] - A[0] > B[1] - B[0]:
        l = A
        s = B
    else:
        l = B
        s = A

    if l[0] <= s[1] and s[1] <= l[1]:
        return True
    if l[0] <= s[0] and s[0] <= l[1]:
        return True

    return False
