"""
幾A幾B的遊戲

思路
a_set = [] 裝答案剩下的值
b_set = [] 裝b沒對到的值

先找出A
for i in a:
    if a[i] == b[i]
        A += 1
找B
for b_set:
    任一b有沒有出現在a_set中
    有則 B += 1
"""


def solve(a, b):
    A = 0
    B = 0
    a_set = []
    b_set = []

    # 找A
    for i in range(len(a)):
        if a[i] == b[i]:
            A += 1
        else:
            a_set.append(a[i])
            b_set.append(b[i])
    # 找B
    for it in b_set:
        if it in a_set:
            B += 1
    return f'{A} A {B} B'


if __name__ == "__main__":
    print(solve('1807', '1807'))  # 4 A 0 B
    print(solve('1807', '7810'))  # 1 A 3 B
    print(solve('1234', '4321'))  # 0 A 4 B
    print(solve('1982', '4981'))  # 2 A 1 B
