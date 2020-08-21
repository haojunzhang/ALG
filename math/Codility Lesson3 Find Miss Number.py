"""
此題是測驗時間複雜度, 需在時間內執行完, 所以可能不可使用回圈

有N個元素裡面隨機有著1 ~ N+1的值
很明顯的有一個數字不在裡面, 請找出那個數

思路
用公式將1 ~ N+1的數加起來 > total
回圈A:
    total一個一個扣除it
回傳剩下的total
"""


def solve(A):
    total = sum([it for it in range(1, len(A)+2)])
    total -= sum([it for it in A])
    return total


if __name__ == "__main__":
    print(solve([2, 3, 1, 5]))  # 4
    print(solve([4, 8, 9, 5, 2, 6, 7, 1]))  # 3
