"""
找出總和到根有等於sum的話回傳True
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


def solve(node, target):
    if node.l == None and node.r == None:
        return node.val == target

    ret1 = False
    if node.l:
        ret1 = solve(node.l, target - node.val)

    ret2 = False
    if node.r:
        ret2 = solve(node.r, target - node.val)

    return ret1 or ret2


if __name__ == "__main__":
    node = get()
    for i in range(11):
        target = i + 1
        print(f'target={target}, {solve(node, target)}')
        # 7 > True
        # 8 > True
        # 10 > True
        # 11 > True
