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


def preorder(node, result):
    # 中左右
    result.append(node.val)

    if node.l:
        preorder(node.l, result)

    if node.r:
        preorder(node.r, result)


def inorder(node, result):
    # 左中右
    if node.l:
        inorder(node.l, result)

    result.append(node.val)

    if node.r:
        inorder(node.r, result)


def postorder(node, result):
    # 左右中
    if node.l:
        postorder(node.l, result)

    if node.r:
        postorder(node.r, result)

    result.append(node.val)


def dfs(node, result):
    result.append(node.val)

    if node.l:
        dfs(node.l, result)

    if node.r:
        dfs(node.r, result)


def bfs(q, result):
    if len(q) == 0:
        return None

    node = q.pop()
    result.append(node.val)

    if node.l:
        q.insert(0, node.l)

    if node.r:
        q.insert(0, node.r)

    bfs(q, result)


def print_tree(node):
    def dfs(node, level, ret):
        if level not in ret:
            ret[level] = []

        ret[level].append(node.val)

        if node.l:
            dfs(node.l, level + 1, ret)

        if node.r:
            dfs(node.r, level + 1, ret)

    ret = {}
    dfs(node, 1, ret)
    text = ''
    for k,  v in ret.items():
        text += '\n' if len(text) != 0 else ''
        text += str(v)
    print(f'{text}')


if __name__ == "__main__":
    node = get()

    # ret = []
    # preorder(node, ret)
    # print(ret)

    # ret = []
    # inorder(node, ret)
    # print(ret)

    # ret = []
    # postorder(node, ret)
    # print(ret)

    # ret = []
    # dfs(node, ret)
    # print(ret)

    # ret = []
    # q = [node]
    # bfs(q, ret)
    # print(ret)
    print_tree(node)
