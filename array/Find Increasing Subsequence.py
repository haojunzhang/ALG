"""
找出遞增子集合
A = [2, 3, 1, 2, 4]
ret = [[1, 2], [1, 4], [2, 3], [1, 2, 4], [2, 3, 4], [3, 4], [2, 4]]

思路
找出A[i]後面可以接哪些值
for i in range(A):
    
    累積A[i]這批最大子集合結果的list
    total_subset = [A[i]]
    
    找出後面比此值大的
    for j in range(i+1,len(A)):
        if A[j] > A[i]:

            加只有2個的
            add([A[i], A[j]])

            加累積的(累積的子集合交給下個i處理)
            total_subset.append(A[j])
            add(total_subset.copy())
"""


def solve(result, A):
    for i in range(len(A)):
        total_subset = [A[i]]
        for j in range(i+1, len(A)):
            if A[j] > A[i]:
                result.append([A[i], A[j]])
                total_subset.append(A[j])
                result.append(total_subset.copy())


if __name__ == '__main__':
    result = []
    solve(result, [2, 3, 1, 2, 4])
    print([list(j) for j in set([tuple(i) for i in result])])
    # 去除重複用set
    # [[1, 2], [1, 4], [2, 3], [1, 2, 4], [2, 3, 4], [3, 4], [2, 4]]
