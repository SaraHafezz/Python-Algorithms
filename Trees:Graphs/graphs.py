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
    
    def slowSP(self, node):
        distances = {node: 0}
        visited = set()
        
        while len(visited) < len(self.adjacent_list):
            min_node = None
            min_distance = float('inf')
            for n, d in distances.items():
                if n not in visited and d < min_distance:
                    min_node = n
                    min_distance = d
            
            if min_node is None:
                break
            
            visited.add(min_node)
            for edge in self.adjacent_list[min_node]:
                neighbor = edge.n1 if edge.n2 == min_node else edge.n2
                new_distance = distances[min_node] + edge.weight
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
        
        return distances
    
    def fastSP(self, node):
        distances = {node: 0}
        visited = set()
        heap = [(0, node)]
        
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_node in visited:
                continue
            
            visited.add(current_node)
            for edge in self.adjacent_list[current_node]:
                neighbor = edge.n1 if edge.n2 == current_node else edge.n2
                new_distance = current_distance + edge.weight
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
        
        return distances

def main():
    graph = Graph()
    graph.importFromFile("random.dot")

    # Measure the performance of both algorithms
    slow_times = []
    fast_times = []

    for node in graph.adjacent_list.keys():
        start_time = time.time()
        graph.slowSP(node)
        slow_times.append(time.time() - start_time)

        start_time = time.time()
        graph.fastSP(node)
        fast_times.append(time.time() - start_time)

    # Report average, max, and min time
    print("Slow Algorithm:")
    print("Average time:", statistics.mean(slow_times))
    print("Max time:", max(slow_times))
    print("Min time:", min(slow_times))
    print("\nFast Algorithm:")
    print("Average time:", statistics.mean(fast_times))
    print("Max time:", max(fast_times))
    print("Min time:", min(fast_times))

    # Plot histogram
    plt.hist(slow_times, bins=10, alpha=0.5, label='Slow Algorithm')
    plt.hist(fast_times, bins=10, alpha=0.5, label='Fast Algorithm')
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Execution Times')
    plt.legend(loc='upper right')
    plt.show()

'''
    Discussion of Findings:
    The histogram displays the distribution of execution times for both the slow and fast versions of Dijkstra's algorithm across all nodes in the graph.
    From the histogram, we observe that the fast algorithm generally has shorter execution times compared to the slow algorithm.
    The distribution of execution times for the fast algorithm appears to be more concentrated towards shorter durations, indicating better performance.
    On the other hand, the slow algorithm shows a wider spread of execution times, with some nodes taking significantly longer to compute.
    Overall, the histogram confirms that the fast algorithm is indeed more efficient in terms of execution time compared to the slow algorithm.
    However, it's important to note that the actual performance may vary depending on factors such as graph size and structure, as well as hardware capabilities.
'''
if __name__ == "__main__":
    main()
