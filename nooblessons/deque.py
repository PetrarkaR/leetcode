class deque:
    
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data=[None]*deque.DEFAULT_CAPACITY
        self._size=0
        self._front=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def queue(self,x):
        if(self._size==len(self._data)):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=x
        self._size+=1
    def first(self):
        if(self.is_empty==True):
            raise Empty('stack empty')
        return self._front
    def dequeue(self):
        if(self.is_empty==True):
            raise Empty('empty')
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        return answer
    def resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0

q=queue()