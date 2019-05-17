class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self,data):
        self.items.append(data)

'''zz=Stack()
zz.push(10)
zz.push(9)
zz.push(30)
zz.push(4)
zz.push(14)
print(zz.items)
print(zz.pop())'''
