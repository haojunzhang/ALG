"""
實作類似java的indexOf
Input: a = "hello", b = "ll"
Output: 2

Input: a = "aaaaa", b = "bba"
Output: -1

思路
for i in a:
    for j in b:
        如a[i+j]與b[j]不同:
            找下個i
"""


def solve(a, b):
    if len(b) > len(a):
        return -1

    for i in range(len(a)):
        for j in range(len(b)):
            # 不同就下一圈i
            if a[i+j] != b[j]:
                break

            # j跑到最後有一樣的
            if j == len(b) - 1:
                return i

            # 找不到
            if i + j == len(a) - 1:
                return -1
    return -1


if __name__ == "__main__":
    print(solve('hello', 'll'))  # 2
    print(solve('aaaaa', 'bba'))  # -1
    print(solve('apple', 'p'))  # 1
    print(solve('abcabcd', 'abcd'))  # 3
