
#undierected
class graph:
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node1, node2=None):
        # Always add node1 first
        if node1 not in self.graph:
            self.graph[node1] = []

        # If node2 is given, add node2 and create edge
        if node2:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    
    def remove_node(self, node1, node2=None):
        if node2:
            # remove edge between node1 and node2
            if node1 in self.graph and node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
            if node2 in self.graph and node1 in self.graph[node2]:
                self.graph[node2].remove(node1)
        else:
            # remove node completely
            if node1 in self.graph:
                for neighbor in list(self.graph[node1]):  # list() to avoid looping issue
                    self.graph[neighbor].remove(node1)
                del self.graph[node1]
    
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

g.remove_node('A', 'B')  # remove edge A <-> B
print(g.graph)
# {'A': ['C'], 'B': ['D'], 'C': ['A'], 'D': ['B']}

g.remove_node('C')       # remove node C
print(g.graph)




# BFS Traversal
print("BFS Traversal:")
g.bfs("A")

# DFS Traversal
print("\nDFS Traversal:")
g.dfs("A")

g.shortest_path('A', 'E')


# Check for cycle
print("\nCycle Detected?", g.has_cycle())




#directed

