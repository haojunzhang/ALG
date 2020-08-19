import datetime
"""
走N階樓梯, 要不是從N-1走1階上來, 要不就是從N-2走2階上來
dp(n) = dp(n-1) + dp(n-2)

陣列
def array_dp1(n):
    初始化陣列a
    a[0] = 1(第1階)
    a[1] = 2(第2階)
    for i in [2..n]
        a[i] = a[i-2] + a[i-1]
    回傳n - 1(第1階存在位置0, 第N階存在n-1)

優化空間array_dp1
    根據n移動a,b n次, 最後回傳a
    [1, 1], 2, 3, 5, 8
    1, [1, 2], 3, 5, 8
    1, 1, [2, 3], 5, 8
def array_dp2(n):
    a, b = 1, 1
    while(n-=1 > 0):
        b += a
        a = b - a
    
遞迴
def recursive_dp1(n):
    n是1回傳1
    n是2回傳2
    回傳(n-1)+(n-2)

改良recursive_dp1
因為有大量的重複運算, 可以用m暫存算過的資料
def recursive_dp2(n, m):
    n是1回傳1
    n是2回傳2
    如n有算過則回傳m[n]
    存(n-1)+(n-2)
    回傳(n-1)+(n-2)

"""


def array_dp1(n):
    a = [0 for i in range(n)]
    a[0] = 1
    a[1] = 2
    for i in range(2, n):
        a[i] = a[i-2] + a[i-1]
    return a[n-1]


def array_dp2(n):
    a, b = 1, 1
    while(n > 0):
        b += a
        a = b - a
        n -= 1
    return a


def recursive_dp1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return recursive_dp1(n-1) + recursive_dp1(n-2)


def recursive_dp2(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    if m[n] > 0:
        return m[n]

    m[n] = recursive_dp2(n - 1, m) + recursive_dp2(n - 2, m)
    return m[n]


if __name__ == '__main__':
    n = 10
    print(array_dp1(n))

    print(array_dp2(n))

    print(recursive_dp1(n))

    m = [0 for i in range(n + 1)]
    print(recursive_dp2(n, m))
