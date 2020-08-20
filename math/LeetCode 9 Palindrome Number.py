"""
判斷是否為回文整數
input : 121
output : true

input : -121
output : false

input : 10
output : false

a = 先找出可以除最左值的10^n數
左值=value除a的整數
右值=value%10
value = value - 左值 - 右值
比較, 直到值剩下1或0位數
"""


def solve(value):
    if value < 0:
        return False
    v = value
    a = 0
    while v >= 10:
        v /= 10
        a += 1
    a = 10 ** a

    while value >= 10:
        l = int(value / a)
        r = value % 10
        if l != r:
            return False

        # 減左值
        value = value - (l*a)

        # 減右值
        value = int(value / 10)

        # 少兩位(左, 右)
        a = int(a / 100)
    return True


if __name__ == "__main__":
    print(solve(121))
    print(solve(-121))
    print(solve(10))
    print(solve(12321))
    print(solve(12345))
