#Undirected graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.print_graph()
#directed graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(3, 0, 4)
g.add_edge(2, 1, 1)
g.print_graph()
#cycle graphs
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
    def dfs_util(self, v, visited, parent):
        visited[v] = True
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1:
                if not visited[i]:
                    if self.dfs_util(i, visited, v):
                        return True
                elif parent != i:
                    return True
        return False
    def is_cyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.dfs_util(i, visited, -1):
                    return True
        return False
g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_edge(3, 0)  
g.add_edge(0, 2) 
g.add_edge(0, 3) 
g.add_edge(0, 4) 
g.add_edge(4, 2)  
g.add_edge(2, 5)  
g.add_edge(2, 1) 
g.add_edge(2, 6) 
g.add_edge(1, 5)  
g.print_graph()
print("\nGraph has cycle:", g.is_cyclic())
#cyclic graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
         if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = 1
          self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
         if 0 <= vertex < self.size:
          self.vertex_data[vertex] = data
    def print_graph(self):
         print("Adjacency Matrix:")
         for row in self.adj_matrix:
            print(' '.join(map(str, row)))
         print("\nVertex Data:")
         for vertex, data in enumerate(self.vertex_data):
          print(f"Vertex {vertex}: {data}")
# Creating a cyclic graph with 4 vertices
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.print_graph()
#Acyclic Graph
class Graph:
    def __init__(self, size):
     self.adj_matrix = [[0] * size for _ in range(size)]
     self.size = size
     self.vertex_data = [''] * size
    def add_edge(self, u, v):
     if 0 <= u < self.size and 0 <= v < self.size:
      self.adj_matrix[u][v] = 1
    def add_vertex_data(self, vertex, data):
     if 0 <= vertex < self.size:
      self.vertex_data[vertex] = data
    def print_graph(self):
     print("Adjacency Matrix:")
     for row in self.adj_matrix:
      print(' '.join(map(str, row)))
     print("\nVertex Data:")
     for vertex, data in enumerate(self.vertex_data):
      print(f"Vertex {vertex}: {data}")
# Creating an acyclic graph with 4 vertices
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()
#Weighted Graph
class Graph:
     def __init__(self, size):
       self.adj_matrix = [[0] * size for _ in range(size)]
       self.size = size
       self.vertex_data = [''] * size
     def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = weight
          self.adj_matrix[v][u] = weight # Assuming the graph is undirected
     def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
         self.vertex_data[vertex] = data
     def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
           print(' '.join(map(str, row)))
           print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
         print(f"Vertex {vertex}: {data}")


g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 5) # Edge from vertex 0 to vertex 1 with weight 5
g.add_edge(0, 2, 3) # Edge from vertex 0 to vertex 2 with weight 3
g.add_edge(0, 3, 7) # Edge from vertex 0 to vertex 3 with weight 7
g.add_edge(1, 2, 2) # Edge from vertex 1 to vertex 2 with weight 2
g.print_graph()





class UndirectedGraph:
         def __init__(self):
             self.graph = {}


         def add_edge(self, u, v):
             if u not in self.graph:
                 self.graph[u] = []
             if v not in self.graph:
                 self.graph[v] = []
             self.graph[u].append(v)
             self.graph[v].append(u)
