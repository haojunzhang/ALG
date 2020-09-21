"""
找出能裝最大容量的值
A[i] = 高度
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

思路
i, j從最邊邊往內縮
回圈
    取最大
    if i < j:
        i++
    else:
        j--
"""


def solve(A):
    ret = 0
    i, j = 0, len(A) - 1
    while i < j:
        ret = max(ret, min(A[i], A[j]) * (j-i))
        if A[i] < A[j]:
            i += 1
        else:
            j -= 1
    return ret


if __name__ == "__main__":
    print(solve([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(solve([3, 5, 2, 9, 1]))  # 10
