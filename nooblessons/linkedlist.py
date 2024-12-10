class linkedStack:
    class node:
        __slots__ = '_element', '_next'
        
        def __init__(self,el,next):
            self._element=el
            self._next=next
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,e):
        self._head= self.node(e, self._head)
        self._size+=1
    def top(self):
        if(self.is_empty()):
            raise Empty('error')
        return self._head._element
    def pop(self):
        if self.is_empty():
            raise Empty('error')
        answer = self._head._element
        self._head=self._head._next
        self._size-=1
        return answer
    
s= linkedStack()
s.push(1)
s.push(2)
s.push(2)
s.push(2)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())