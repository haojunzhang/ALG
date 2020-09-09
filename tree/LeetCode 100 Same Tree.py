"""
判斷是否為相同的樹
"""


class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r


def get():
    """
             1
           /   \
          2     3
         / \   / \
        4   5 6   7  
    """
    n4 = Node(4, None, None)
    n5 = Node(5, None, None)
    n6 = Node(6, None, None)
    n7 = Node(7, None, None)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    return n1


def solve(n1, n2):
    # 都是None = 相同
    if n1 == None and n2 == None:
        return True

    # 其中一個樹沒左或右
    if (n1.l == None and n2.l != None) or (n1.l != None and n2.l == None):
        return False

    # 值不一樣
    if n1.val != n2.val:
        return False

    return solve(n1.l, n2.l) and solve(n1.r, n2.r)


if __name__ == "__main__":
    n1 = get()
    n2 = get()
    print(solve(n1, n2))  # True

    n2.r.r.val = 9
    print(solve(n1, n2))  # False
