"""
求正方形最大邊長
有兩隻木頭A, B
長度分別為21, 10, 他們可以為成最大的正方形的邊長為7
因為可以把A分成3份7, B切掉3得到7
A=13, B=11 >>> 5
A=2, B=1 >>> 0
A=1, B=8 >>> 2

思路
回圈直到ret = 0:
    因為是正方形所以有4邊
    看兩塊木頭可以被長度為ret的木頭分幾等分
    A可以被分的次數=int(A / ret)
    B可以被分的次數=int(A / ret)
    如果 A的次數+B的次數 >= 4(可圍成正方形)
    就回傳該ret木頭長度
"""


def solution(A, B):
    # write your code in Python 3.6
    ret = int((A + B) / 4)
    while ret != 0:
        if (4 - int(A / ret) - int(B / ret)) <= 0:
            return ret
        ret -= 1
    return 0
