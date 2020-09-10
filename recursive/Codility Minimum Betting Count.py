"""
賭博遊戲
N=要贏到的硬幣數量
K=可以all-in的次數
從1枚硬幣開始
每次都可選擇下1或all-in

思路
利用二元樹, 分別以下1枚和all-in灑下去, 
回傳條件為達到N目標的數量, 且深度最短的
"""


def solution(N, K):
    if N == 1:
        return 0
    return solve(N, K, 0, 1)


def solve(N, K, level, coin):
    if coin >= N:
        return level

    coin1 = coin + 1
    ret1 = solve(N, K, level + 1, coin1)

    ret2 = 99999
    if K > 0:
        coin2 = coin * 2
        ret2 = solve(N, K - 1, level + 1, coin2)
    return min(ret1, ret2)
