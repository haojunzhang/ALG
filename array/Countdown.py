"""
2020 Kickstart Round C Countdown
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2
Input
3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100

Output
Case #1: 2
Case #2: 0
Case #3: 1

N = 從N到1遞減的子集合
找出A中有幾個N的子集合
N = 3 >> [3, 2, 1]
A = [1, 2, 3, 7, 9, '3, 2, 1', 8, '3, 2, 1']
return 2

先求出N的集合s
跑回傳注意終止index
['1, 2, 3', 7, 9, 3, 2, 1, 8, 3, 2, 1]
[1, '2, 3, 7', 9, 3, 2, 1, 8, 3, 2, 1]
['1, 2, '3, 7, 9', 3, 2, 1, 8, 3, 2, 1]
...
想像一個框一個一個往右移動檢查
"""

def solve(N, A):
    ans = 0
    s = [N-it for it in range(N)]
    for i in range(len(A) - (N - 1)):
        ok = True
        for j in range(len(s)):
            if A[i+j] != s[j]:
                ok = False
                break
        if ok:
            ans += 1
    return ans

if __name__ == '__main__':
    print(solve(3, [1, 2, 3, 7, 9, 3, 2, 1, 8, 3, 2, 1])) # 2
    print(solve(2, [101, 100, 99, 98])) # 0
    print(solve(6, [100, 7, 6, 5, 4, 3, 2, 1, 100])) # 1