import sys


class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CList(object):
    def __init__(self):
        self.last = None # 마지막 노드
    
    def insert(self, data):
        newNode = Node(data, None)
        if not self.last:
            newNode.next = newNode
            self.last = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode
            self.last = newNode # 이 과정이 있으면 <뒤> 삽입, 없으면 <앞> 삽입
        
    def delete(self, data):
        if self.last.data == data:  # 삭제할 노드가 첫 번째 노드일 때
            current = self.last
            self.last = self.last.next
            while self.last.next != current:
                self.last = self.last.next          
            self.last.next = current.next                  
            del current
            return data

        current = self.last
        while current.next != self.last:
            pre = current
            current = current.next
            if current.data == data:
                pre.next = current.next
                del current
                return data
    
    def print_yosep(self, N, K):
        L = []
        p = self.last
        for _ in range(N):
            for _ in range(K):
                p = p.next
            L.append(self.delete(p.data))
        return L

N, K = map(int, sys.stdin.readline().strip().split())
cl = CList()
for i in range(1, N+1):
    cl.insert(i)

L = cl.print_yosep(N, K)
print('<',end='')
print(', '.join(str(x) for x in L),end='')
print('>')