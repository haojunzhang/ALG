"""
鏡射二元樹
"""
from traversal import print_tree


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


def solve(node):

    tmp = node.l
    node.l = node.r
    node.r = tmp

    if node.l:
        solve(node.l)

    if node.r:
        solve(node.r)


if __name__ == "__main__":
    n1 = get()
    solve(n1)
    print_tree(n1)
