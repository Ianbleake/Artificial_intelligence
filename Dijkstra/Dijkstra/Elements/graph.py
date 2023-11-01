import sys
from .node import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name: str, line: str) -> None:
        if name in self.nodes:
            return
        node = Node(name, line)
        self.nodes[node.name] = node

    def add_connection(self, node_name: str, node2_name: str, weight: int) -> None:
        self.nodes[node_name].add_connection(self.nodes[node2_name], weight)
        self.nodes[node2_name].add_connection(self.nodes[node_name], weight)

    def dijkstra(self, start: str, end: str) -> list:
        distances = {name: sys.maxsize for name in self.nodes}
        distances[start] = 0
        visited = set()

        while visited != set(self.nodes.keys()):
            unvisited = {name: distance for name, distance in distances.items() if name not in visited}
            current_node = min(unvisited, key=unvisited.get)
            visited.add(current_node)

            for neighbor, weight in self.nodes[current_node].connections:
                if distances[current_node] + weight < distances[neighbor.name]:
                    distances[neighbor.name] = distances[current_node] + weight

        path = []
        current = end
        while current != start:
            path.insert(0, current)
            for neighbor, weight in self.nodes[current].connections:
                if distances[current] == distances[neighbor.name] + weight:
                    current = neighbor.name
                    break
        path.insert(0, start)
        return path