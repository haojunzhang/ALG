"""
             1
           /   \
          2     3
         / \   / \
        4   5 6   7  
"""


class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r


def get():
    n4 = Node(4, None, None)
    n5 = Node(5, None, None)
    n6 = Node(6, None, None)
    n7 = Node(7, None, None)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    return n1


def preorder(node):
    # 中左右
    print(node.val)

    if node.l:
        preorder(node.l)

    if node.r:
        preorder(node.r)


def inorder(node):
    # 左中右
    pass


def postorder(node):
    # 左右中
    pass


def dfs(node):
    pass


def bfs(node):
    pass


if __name__ == "__main__":
    node = get()

    preorder(node)
    # inorder(node)
    # postorder(node)
    # dfs(node)
    # bfs(node)
