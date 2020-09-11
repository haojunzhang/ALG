"""
判斷是否為二元平衡樹

二元平衡樹  :對於每個節點，它左右子樹的高度相差必須小於等於一。

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
              4   5  
    """
    n4 = Node(4, None, None)
    n5 = Node(5, None, None)

    n2 = Node(2, None, None)
    n3 = Node(3, n4, n5)

    n1 = Node(1, n2, n3)
    return n1


def get2():
    """
             1
           /   \
          2     3
         / \
        4   5  
       / \
      6   7
    """
    n6 = Node(6, None, None)
    n7 = Node(7, None, None)

    n4 = Node(4, n6, n7)
    n5 = Node(5, None, None)

    n2 = Node(2, n4, n5)
    n3 = Node(3, None, None)

    n1 = Node(1, n2, n3)
    return n1


def solve(node):
    if node == None:
        return True

    if node.l == None and node.r == None:
        return True

    r1 = find_height(node.l)
    r2 = find_height(node.r)

    return False if abs(r1 - r2) > 1 else True


def find_height(node):
    if node == None:
        return 0
    return 1 + max(find_height(node.l), find_height(node.r))


if __name__ == "__main__":
    node = get()
    print(solve(node))  # True
    node = get2()
    print(solve(node))  # False
