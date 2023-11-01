class Node:
    def __init__(self, name: str, line: str) -> None:
        self.name = name
        self.line = line
        self.connections = []

    def add_connection(self, node: "Node", weight: int) -> None:
        self.connections.append((node, weight))
