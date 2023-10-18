class GraphDFS:
    
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
            visited = []
        
        visited.append(start)
        
        for n in sorted(self.get_neighbors(start)):
            if n not in visited:
                self.dfs(n, visited)
        
        return visited
