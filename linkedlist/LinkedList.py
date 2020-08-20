class Node:
    def __init__(self):
        self.val = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def size(self):
        return self.length

    def add(self, val):
        n = Node()
        n.val = val

        if self.head:
            cur = self.head
            while cur:
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = n
            self.length += 1
        else:
            # 如果本來是空的, 初始化head
            self.head = n
            self.length += 1

    def get(self, i):
        if i >= self.length:
            raise Exception('index out of range')
        if i == 0:
            return self.head.val

        # 從頭開始, 移動i個指標
        cur = self.head
        for it in range(i):
            cur = cur.next

        return cur.val

    def remove(i):
        pass

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev

    def __str__(self):
        l = []
        cur = self.head
        while cur:
            l.append(str(cur.val))
            cur = cur.next
        return '[' + ', '.join(l) + ']'


if __name__ == '__main__':
    l = LinkedList()
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.add(7)
    print(l)
    l.reverse()
    print(l)
