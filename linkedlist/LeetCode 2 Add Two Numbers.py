"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
從個位數開始

思路

"""


class Node:
    def __init__(self, next, val):
        self.next = next
        self.val = val


def get1():
    n3 = Node(None, 3)
    n4 = Node(n3, 4)
    n2 = Node(n4, 2)
    return n2


def get2():
    n4 = Node(None, 4)
    n6 = Node(n4, 6)
    n5 = Node(n6, 5)
    return n5


def solve(n1, n2):
    ret = Node(None, -1)
    cur = ret
    tmp = 0  # 進位值
    while n1 or n2:
        v1 = n1.val if n1 else 0
        v2 = n2.val if n2 else 0
        total_val = v1 + v2 + tmp
        tmp = 1 if total_val >= 10 else 0  # 進位值

        cur.next = Node(None, total_val % 10)
        cur = cur.next

        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None

    # 最後一圈
    if tmp == 1:
        cur.next = Node(None, 1)

    return ret.next


def show(n):
    cur = n
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == "__main__":
    ret = solve(get1(), get2())
    show(ret)
