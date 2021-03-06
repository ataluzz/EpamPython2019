"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""
#task1

from queue import Queue
import collections

class GraphIterator:
    
    def __init__(self, graph):
        self.E = E
        self.queue = Queue()
        self.keys = list(E.keys())
        self.visited = [tuple(self.E.keys())[0]]
        self.queue.put(tuple(self.E.keys())[0])
        
    def __next__(self):
        while not self.queue.empty():
            k = self.queue.get()
            values = self.E[k]
            for val in values:
                if val not in self.visited:
                    self.visited.append(val)
                    self.queue.put(val)
            return k
        raise StopIteration
        
    def __iterator__(self):
        return self
                    
                
                
class Graph:
    def __init__(self, E):
        self.E = E
    
    def __iter__(self):
        return GraphIterator(self)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)
