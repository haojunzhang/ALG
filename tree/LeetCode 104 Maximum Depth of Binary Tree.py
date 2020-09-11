"""
找最大深度

思路

如是None回傳0
否則1+最大值(左右遞迴)
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
    return 1 + max(solve(node.l), solve(node.r))


if __name__ == "__main__":
    node = get()
    print(solve(node))
