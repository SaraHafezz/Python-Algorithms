import heapq
import time
import statistics
import matplotlib.pyplot as plt

class GraphNode:
    def __init__(self, data):
        self.data = data

class GraphEdge:
    def __init__(self, n1, n2, weight):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def addNode(self, data):
        new_node = GraphNode(data)
        self.adjacent_list[new_node] = []
        return new_node

    def removeNode(self, data):
        for node in self.adjacent_list.keys():
            if node.data == data:
                del self.adjacent_list[node]
                break

        for node, edges in self.adjacent_list.items():
            self.adjacent_list[node] = [edge for edge in edges if edge.n1.data != data and edge.n2.data != data]

    def addEdge(self, n1, n2, weight = 1000000000):
        new_edge = GraphEdge(n1, n2, weight)
        self.adjacent_list[n1].append(new_edge)
        self.adjacent_list[n2].append(new_edge)

    def removeEdge(self, n1, n2):
        edges_to_remove = []
        for edge in self.adjacent_list[n1]:
            if (edge.n1 == n1 and edge.n2 == n2) or (edge.n1 == n2 and edge.n2 == n1):
                edges_to_remove.append(edge)
        for edge in edges_to_remove:
            self.adjacent_list[n1].remove(edge)
            self.adjacent_list[n2].remove(edge)

    def importFromFile(self, file):
        # Clear existing nodes and edges
        self.adjacent_list.clear()

        # Read the GraphViz file and extract nodes and edges
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if '->' in line:  # Edge definition
                    nodes = line.split('->')
                    n1 = self.addNode(nodes[0].strip())
                    n2 = self.addNode(nodes[1].strip())
                    self.addEdge(n1, n2)
                elif '--' in line:  # Undirected edge definition
                    nodes = line.split('--')
                    n1 = self.addNode(nodes[0].strip())
                    n2 = self.addNode(nodes[1].strip())
                    self.addEdge(n1, n2)

    def dfs(self, start):
        visited = set()
        stack = [start]
        dfs_order = []

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                dfs_order.append(current_node)
                for edge in self.adjacent_list[current_node]:
                    neighbor = edge.n1 if edge.n2 == current_node else edge.n2
                    if neighbor not in visited:
                        stack.append(neighbor)

        return dfs_order

class Graph2:
    def __init__(self):
        self.adjacency_matrix = {}

    def addNode(self, data):
        if data not in self.adjacency_matrix:
            self.adjacency_matrix[data] = {}
            for node in self.adjacency_matrix:
                self.adjacency_matrix[node][data] = 0
            self.adjacency_matrix[data][data] = 0

    def removeNode(self, data):
        if data in self.adjacency_matrix:
            del self.adjacency_matrix[data]
            for node in self.adjacency_matrix:
                del self.adjacency_matrix[node][data]

    def addEdge(self, n1, n2, weight = 1000000000):
        if n1 in self.adjacency_matrix and n2 in self.adjacency_matrix:
            self.adjacency_matrix[n1][n2] = weight
            self.adjacency_matrix[n2][n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency_matrix and n2 in self.adjacency_matrix:
            self.adjacency_matrix[n1][n2] = 0
            self.adjacency_matrix[n2][n1] = 0

    def dfs(self, start):
        visited = set()
        stack = [start]
        dfs_order = []

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                dfs_order.append(current_node)
                for neighbor, weight in self.adjacency_matrix[current_node].items():
                    if neighbor not in visited and weight != 0:
                        stack.append(neighbor)

        return dfs_order

def main():
    graph = Graph()
    graph.importFromFile("random.dot")

    # Create Graph2 object and populate it with the same data
    graph2 = Graph2()
    for node in graph.adjacent_list.keys():
        graph2.addNode(node.data)
    for node, edges in graph.adjacent_list.items():
        for edge in edges:
            graph2.addEdge(node.data, edge.n1.data if edge.n2 == node else edge.n2.data, edge.weight)

    # Measure the performance of dfs() on both implementations
    dfs_times_graph = []
    dfs_times_graph2 = []

    for _ in range(10):
        start_time = time.time()
        for node in graph.adjacent_list.keys():
            graph.dfs(node)
        dfs_times_graph.append(time.time() - start_time)

        start_time = time.time()
        for node in graph2.adjacency_matrix.keys():
            graph2.dfs(node)
        dfs_times_graph2.append(time.time() - start_time)

    # Report maximum, minimum, and average time
    print("DFS on Graph:")
    print("Maximum time:", max(dfs_times_graph))
    print("Minimum time:", min(dfs_times_graph))
    print("Average time:", sum(dfs_times_graph) / len(dfs_times_graph))

    print("\nDFS on Graph2:")
    print("Maximum time:", max(dfs_times_graph2))
    print("Minimum time:", min(dfs_times_graph2))
    print("Average time:", sum(dfs_times_graph2) / len(dfs_times_graph2))


    """
    The results show that DFS traversal on Graph2 (using adjacency matrix) is generally faster than on Graph (using adjacency list).
    This is likely because adjacency matrix allows for constant-time lookup of edges, whereas adjacency list requires iterating over a list of neighbors.
    Additionally, adjacency matrix consumes more memory compared to adjacency list, but it provides faster edge lookup.
    In this case, the performance benefit of faster lookup outweighs the memory reqirements, resulting in faster DFS traversal.
    """

if __name__ == "__main__":
    main()
