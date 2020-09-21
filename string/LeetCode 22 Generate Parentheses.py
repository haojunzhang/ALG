"""
根據傳入的n回傳由n組合法括弧組成的集合
n = 3
return:
    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]

思路
利用遞迴解, left, right=剩餘可用括弧數量, 最後一定只有3個左與右括弧, 且不可left > right,
例如left=3, right=2, 代表用了一個')', 這樣就不合法
"""


def solve(n):
    ret = []
    helper(n, n, '', ret)
    return ret


def helper(left, right, text, ret):
    if left < 0 or right < 0 or left > right:
        return
    # 結束了
    if left == 0 and right == 0:
        ret.append(text)
        return
    helper(left - 1, right, text + '(', ret)  # 用了一個左括弧
    helper(left, right - 1, text + ')', ret)  # 用了一個右括弧


if __name__ == "__main__":
    print(solve(3))
