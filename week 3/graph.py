class graph:
    
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
    
    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        if node2 in self.graph and node1 in self.graph[node2]:
            self.graph[node2].remove(node1)
            
    def remove_node(self, node):
        if node in self.graph:
            for neighbor in self.graph[node]:
                self.graph[neighbor].remove(node)
            del self.graph[node]
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend([n for n in self.graph[node] if n not in visited])
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            print(start, end=' ')
            visited.add(start)
            
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

    def shortest_path(self, start, end):
        queue = [(start, [start])]
        visited = set()

        while queue:
            node, path = queue.pop(0)
            if node == end:
                return path
            if node in visited:
                continue
            visited.add(node)
            queue += [(n, path + [n]) for n in self.graph[node] if n not in visited]
        return None

    
    def has_cycle(self):
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        for node in self.graph:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False
    
    def print_graph(self):
        for node in self.graph:
            print(f'{node} --> {self.graph[node]}')






g = graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.print_graph()

print("\nRemoving edge A-B and node C...")
g.remove_edge("A", "B")
g.remove_node("C")
g.print_graph()

# BFS Traversal
print("BFS Traversal:")
g.bfs("A")

# DFS Traversal
print("\nDFS Traversal:")
g.dfs("A")

# Check for cycle
print("\nCycle Detected?", g.has_cycle())
