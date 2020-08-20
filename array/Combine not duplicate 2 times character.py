"""
將AAAA, BBBB組合起來, 但不能有任一重複大於2次

思路
以遞迴方式散下去, 當組起來後重複次數大於2次則跳過, 反之組起來
再散A, B兩種組合下去, 直到A, B用完
a = 'AAAA'
b = 'BBBB'
result = [] 裝結果
跑A開頭
t1 = 'A'
def dfs(result, text, a, b)
    # result : 裝結果
    # text : 累積的字串
    # a, b : 還有多少可用的字串(會慢慢減少)
    當a, b都是空的, 裝結果, 結束
    如果組上a重複次數大於2則結束, 反之組上一個A, 減少a, text增加, 下一圈
    如果組上b重複次數大於2則結束, 反之組上一個B, 減少b, text增加, 下一圈
"""


def is_duplicate(text):
    return len(text) > 2 and len(set(text[-3:])) == 1


def dfs(result, text, a, b):
    if len(a) == 0 and len(b) == 0:
        result.append(text)
        return None

    if len(a) != 0:
        text += a[0]
        if is_duplicate(text):  # 尾巴重複3個字元
            return None
        dfs(result, text, a[1:], b)

    if len(b) != 0:
        text += b[0]
        if is_duplicate(text):  # 尾巴重複3個字元
            return None
        dfs(result, text, a, b[1:])


if __name__ == '__main__':
    result = []
    a = 'AAA'
    b = 'BBB'
    text = ''
    dfs(result, text, a, b)
    print(result)
