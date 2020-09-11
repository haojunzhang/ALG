"""
找出最小深度

思路
如左邊是空, 右邊 1+且遞迴
如右邊是空, 左邊 1+且遞迴
如果兩邊都不是空, 則1+最小值(左右遞迴)
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
               / \
              6   7  
             / \
            8   9    
    """
    n8 = Node(8, None, None)
    n9 = Node(9, None, None)

    n6 = Node(6, n8, n9)
    n7 = Node(7, None, None)

    n2 = Node(2, None, None)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    return n1


def solve(node):
    if node == None:
        return 0

    if node.l == None:
        return 1 + solve(node.r)

    if node.r == None:
        return 1 + solve(node.l)

    return 1 + min(solve(node.l), solve(node.r))


if __name__ == "__main__":
    node = get()
    print(solve(node))
