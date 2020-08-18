def solve(N, A):
    ans = 0
    s = [N-it for it in range(N)]
    for i in range(len(A)-(N-1)):
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