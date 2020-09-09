"""
找出root到根的路徑
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


def solve(node, text, ret):
    if node.l == None and node.r == None:
        ret.append(text)

    if node.l:
        solve(node.l, text + '>' + str(node.l.val), ret)

    if node.r:
        solve(node.r, text + '>' + str(node.r.val), ret)


if __name__ == "__main__":
    node = get()
    ret = []
    solve(node, str(node.val), ret)
    print(ret)  # ['1>2>4', '1>2>5', '1>3>6', '1>3>7']
