import sys


class Node(object):
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.cur = self.tail
    
    def insert(self, node, data):
        tmp_prev = node.prev
        newNode = Node(data, tmp_prev, node)
        tmp_prev.next = newNode
        node.prev = newNode
        
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
    
    def print_list(self):
        target = self.head.next
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, end='')
            else:
                print(target.data)
            target = target.next


for i in range(int(sys.stdin.readline().strip())):
    dl = DList()
    for o in sys.stdin.readline().strip():
        if o == "<":
            if dl.cur.prev.prev:
                dl.cur = dl.cur.prev
        elif o == ">":
            if dl.cur.next:
                dl.cur = dl.cur.next
        elif o == "-":
            if dl.cur.prev.prev:
                dl.delete(dl.cur.prev)
        else:
            dl.insert(dl.cur, o)
    dl.print_list()