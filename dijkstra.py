import heapq
def dijkstra(graph, start):
    #pq: A priority queue (using Python's heapq), initialized with the starting node and distance 0.
    #distances: A dictionary to track the shortest distance from the start node to each node. 
    #We initialize all nodes to infinity (float('inf')), except the start node, 
    #which gets a distance of 0
    pq = [(0,start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        #We pop the node with the smallest distance from the priority queue.
        #If the queue is empty, the algorithm stops.
        current_distance, current_node = heapq.heapop(pq)
        if current_distance > distances[current_node]:
            continue
        # If we’ve already found a shorter path to this node, we skip it (important for performance).
        for neighbor, weight in graph[current_node].items():
            #We iterate over all neighboring nodes of the current node.
            #weight is the edge weight (distance/cost) to that neighbor.
            #We calculate the total distance from the start node to this neighbor.
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq,(distance,neighbor))

    return distances


# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print("Shortest paths from", start_node, ":", shortest_paths)
