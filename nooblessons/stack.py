class stack:
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,x):
        self._data.append(x)
    def top(self):
        if(self.is_empty==True):
            raise Empty('stack empty')
        return self._data[-1]
    def pop(self):
        if(self.is_empty==True):
            raise Empty('empty')
        return self._data.pop()
def reverse_file(filename):
        S=stack()
        original=open(filename)
        for line in original:
            S.push(line.rstrip('\n'))
        original.close()
        output=open(filename,'w')
        while not S.is_empty():
            output.write(S.pop()+'\n')
        output.close()
def is_matched(expr):
    left='({['
    right=')}]'
    s=stack()
    for c in expr:
        if c in left:
            s.push(c)
        elif c in right:
            if s.is_empty():
                return False
            if(right.index(c)!=left.index(s.pop())):
                return False
    return s.is_empty()
print(is_matched(((()))))
s=stack()
s.push(3)
s.push(5)
reverse_file(r"C:\Users\swagg\OneDrive\Desktop\leetcode\nooblessons\text.txt")
