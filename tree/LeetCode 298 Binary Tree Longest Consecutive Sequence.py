"""
輸出最長連續的路徑的長度
"""


class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r


def get1():
    """
             1
               \
                3
               / \
              6   4
                   \
                    5 
    """
    n5 = Node(5, None, None)

    n4 = Node(4, None, n5)
    n6 = Node(6, None, None)

    n3 = Node(3, n4, n6)

    n1 = Node(1, None, n3)
    return n1

def get2():
    """
             1
           /   \
                3
               / \
              6   4
                   \
                    5 
    """
    n5 = Node(5, None, None)

    n4 = Node(4, None, n5)
    n6 = Node(6, None, None)

    n3 = Node(3, n4, n6)

    n1 = Node(1, None, n3)
    return n1


def solve(node, pre_v, count, ret):
    if node.val == pre_v + 1:
        count += 1
    else:
        count = 1

    ret[0] = max(ret[0], count)

    if node.l:
        solve(node.l, node.val, count, ret)

    if node.r:
        solve(node.r, node.val, count, ret)


if __name__ == "__main__":
    node = get1()
    ret = [0]
    solve(node, node.val, 0, ret)
    print(ret[0])  # 3
