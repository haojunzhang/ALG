"""
Jump Game
初始在i = 0
可以移動0~A[i]步
如果可以到最後一個位置則回傳true
1.使用貪婪演算法(每次都跳最遠)
2.其他DFS之類的

max_i = 目前最遠可到達位置最大值
for i in range(len(A)):
    如目前的位置i, 如果比最大值大(最遠只能跳到這), 代表目前的位置到不了, 所以更不可能到最後一格, 回傳false
    算出這個位置最遠可跳到哪
    算出來後和最大值比較取最大
    如果可以跳超過最後一個位置直接回傳True
回傳true
"""


def solve(A):
    max_i = 0
    for i in range(len(A)):
        if i > max_i:
            return False
        max_i = max(i + A[i], max_i)

        # 如果可以跳超過最後一個位置直接回傳True
        if max_i >= (len(A) - 1):
            return True
    return True


if __name__ == '__main__':
    print(solve([2, 3, 1, 1, 4]))  # True
    print(solve([3, 0, 0, 2, 0, 1]))  # True
    print(solve([1, 1, 1, 1, 1]))  # True
    print(solve([1, 1, 0, 1, 1]))  # False
    print(solve([3, 2, 1, 0, 4]))  # False
    print(solve([0, 1, 2]))  # False
