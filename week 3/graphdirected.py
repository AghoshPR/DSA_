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
        # Only one direction for directed graph
    
    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        # Only remove one direction for directed graph
            
    def remove_node(self, node):
        if node in self.graph:
            # Remove the node and its outgoing edges
            del self.graph[node]
            
            # Remove incoming edges to this node
            for source in self.graph:
                if node in self.graph[source]:
                    self.graph[source].remove(node)
    
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
        # For directed graph, we need to track nodes in the current path
        visited = set()      # All nodes visited overall
        rec_stack = set()    # Nodes in current DFS path
        
        def dfs_cycle(node):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:  # If neighbor is in recursion stack, there's a cycle
                    return True
            
            rec_stack.remove(node)  # Remove from current path
            return False
        
        for node in self.graph:
            if node not in visited:
                if dfs_cycle(node):
                    return True
        return False
    
    def print_graph(self):
        for node in self.graph:
            print(f'{node} --> {self.graph[node]}')
    
    # Additional methods useful for directed graphs
    
    def in_degree(self, node):
        """Count how many edges point to this node"""
        count = 0
        for source in self.graph:
            if node in self.graph[source]:
                count += 1
        return count
    
    def out_degree(self, node):
        """Count how many edges originate from this node"""
        if node in self.graph:
            return len(self.graph[node])
        return 0

    def topological_sort(self):
        """Return nodes in topological order (only for DAG - directed acyclic graph)"""
        if self.has_cycle():
            return None  # Cannot perform topological sort on cyclic graph
            
        visited = set()
        result = []
        
        def dfs_topo(node):
            visited.add(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_topo(neighbor)
            
            result.insert(0, node)  # Add to front of result after visiting all neighbors
        
        for node in self.graph:
            if node not in visited:
                dfs_topo(node)
                
        return result


# Example usage
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

# In-degree and out-degree
print("\nIn-degree of B:", g.in_degree("B"))
print("Out-degree of A:", g.out_degree("A"))

# Create a DAG for topological sort example
dag = graph()
dag.add_edge("A", "B")
dag.add_edge("A", "C")
dag.add_edge("B", "D")
dag.add_edge("C", "D")

# Topological Sort
print("\nTopological Sort:", dag.topological_sort())