#task1

from queue import Queue
import collections

class GraphIterator(collections.abc.Iterator):
    def __init__(self, graph):
        self.E = E
        self.queue = Queue()
        self.keys = list(E.keys())
        self.visited = [self.keys[0]]
        self.queue.put(self.keys[0])
        
    def __next__(self):
        while self.queue:
            k = self.queue.get()
            values = self.E[k]
            for val in values:
                if val not in self.visited:
                    self.visited.append(val)
                    self.queue.put(val)
            return k
        raise StopIteration
                    
                
                
class Graph(collections.abc.Iterable):
    def __init__(self, E):
        self.E = E
    
    def __iter__(self):
        return GraphIterator(self)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)
