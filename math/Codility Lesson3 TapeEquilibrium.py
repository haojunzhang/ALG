"""
求出最小的絕對值
P將整個A切兩等份
求出這兩等份個別加總後取絕對值
0 < P < N
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 4
A[4] = 3

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7

思路
從i = 0開始
l=0 左半邊加總(先加出來)
r=sum(A) 右半邊加總(先加出來)
m = abs(l - r) 最小值
回圈A 從i=1開始:
    l += A[i]  左邊一圈一圈加
    r -= A[i]  右邊一圈一圈減
    m = min(abs(l-r), m) 找最小
return m
最好是畫出圖了解i跑到哪注意需要i-1
最小值m需設大值, 原本用abs(l-r), 但出現[-1000,1000]這種過不了
"""


def solve(A):
    l = 0
    r = sum(A)
    m = 99999
    for i in range(1, len(A)):
        l += A[i-1]
        r -= A[i-1]
        m = min(abs(l-r), m)
    return m


if __name__ == "__main__":
    print(solve([3, 1, 2, 4, 3]))  # 1
