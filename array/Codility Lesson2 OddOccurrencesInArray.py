"""
找出沒被配對的值
A=[9, 3, 9, 3, 9, 7, 9]
A[0] & A[2]
A[1] & A[3]
A[4] & A[6]
A[5] = 7 沒被配到

思路
建一個set > s
迴圈A
    如該值沒出現在s則add, 有則remove
最後看s剩下誰
"""


def solve(A):
    s = set()
    for it in A:
        if it in s:
            s.remove(it)
        else:
            s.add(it)
    return s.pop()


if __name__ == "__main__":
    print(solve([9, 3, 9, 3, 9, 7, 9]))  # 7
    print(solve([0]))  # 0
    print(solve([0, 1, 0]))  # 1
