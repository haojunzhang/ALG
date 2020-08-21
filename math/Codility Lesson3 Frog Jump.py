"""
此題是測驗時間複雜度, 需在時間內執行完, 所以可能不可使用回圈

X = 10  起點
Y = 85  終點
D = 30  一次跳躍距離
return 3 跳>=終點所需次數

思路
(終點-起點) / 一次距離
除完再無條件進位到整數


"""


def solve(X, Y, D):
    r = (Y - X) / D
    if r == int(r):
        return int(r)
    else:
        return int(r) + 1


if __name__ == "__main__":
    print(solve(10, 85, 30))  # 3
    print(solve(50, 200, 1000))  # 1
    print(solve(10, 1000, 1))  # 990
