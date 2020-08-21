"""
Count Div
A, B, K 
在A,B區間中找出可被K整除的數量

思路
找出>=A且是K的倍數 >> a
找出<=B且是K的倍數 >> b
回傳(b-a)/K+1

[0,0,11]有符合1個 0 % 11 = 0
"""


def solve(A, B, K):
    if A == B and A == 0:
        return 1

    while A % K != 0:
        A += 1
    while B % K != 0:
        B -= 1

    if A > B:
        return 0

    return int((B-A) / K + 1)


if __name__ == "__main__":
    print(solve(6, 11, 2))  # 3
    print(solve(6, 12, 2))  # 4
    print(solve(5, 11, 2))  # 3
    print(solve(5, 12, 2))  # 4
    print(solve(0, 0, 11))  # 0
    print(solve(1, 1, 11))  # 0
