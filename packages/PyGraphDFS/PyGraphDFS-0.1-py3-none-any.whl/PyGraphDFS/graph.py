class Graph:
    
    def __init__(self):
        self.graph = {}  
        
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v) 
    
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        
        for n in self.graph[start]:
            if n not in visited:
                self.graph(n, visited)