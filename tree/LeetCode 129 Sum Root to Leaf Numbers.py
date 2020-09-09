"""
加總到leaf節點的數
以下面例子
124 + 125 + 136 + 137 = 522
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


def solve(node, value, ret):
    value = value * 10 + node.val
    if node.l == None and node.r == None:
        ret.append(value)

    if node.l:
        solve(node.l, value, ret)

    if node.r:
        solve(node.r, value, ret)


if __name__ == "__main__":
    node = get()
    ret = []
    solve(node, 0, ret)
    print(sum(ret))  # 522
