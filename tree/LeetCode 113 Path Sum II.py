"""
找出總和到根有等於sum的話回傳符合的結果
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
        4   5 6   3  
    """
    n4 = Node(4, None, None)
    n5 = Node(5, None, None)
    n6 = Node(6, None, None)
    n7 = Node(3, None, None)

    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    n1 = Node(1, n2, n3)
    return n1


def solve(node, target, data, ret):
    data = data.copy()
    if node.l == None and node.r == None:
        if node.val == target:
            data.append(node.val)
            ret.append(data)
        return None

    data.append(node.val)

    if node.l:
        solve(node.l, target - node.val, data, ret)

    if node.r:
        solve(node.r, target - node.val, data, ret)


if __name__ == "__main__":
    node = get()
    ret = []
    solve(node, 7, [], ret)
    print(ret)
    # [
    #   [1, 2, 4],
    #   [1, 3, 3]
    # ]
