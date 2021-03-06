import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self,data,priority):
        heapq.heappush(self.qlist, (priority,data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    def getFrontMost(self):
        return self.qlist[-1]
    def getRearMost(self):
        return self.qlist[0]
    
q = PriorityQueue()
q.enqueue(98, 1)
q.enqueue(20, 2)
q.enqueue(11, 3)
q.enqueue(55, 4)
q.enqueue(7, 5)

print(q.getFrontMost())
print(q.getRearMost())
print(q.qlist)
