from collections import defaultdict

FILENAME = "input.txt"

class Node:
    def __init__(self, name: str):
        self.name = name
        self._is_big = name.isupper()

    def is_big(self) -> bool:
        return self._is_big

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

class Graph:
    def __init__(self):
        self.nodes = set()
        self.neighbors = defaultdict(list)

    def add_edge(self, node1: Node, node2: Node):
        self.nodes.add(node1.name)
        self.nodes.add(node2.name)

        self.neighbors[node1.name].append(node2)
        self.neighbors[node2.name].append(node1)

    def _count_paths_helper(self, current_node: Node, visited_set: set[str], is_small_visited: bool, is_visited_twice: bool) -> int:
        if current_node.name in visited_set:
            if is_visited_twice or current_node.name == "start":
                return 0

            is_visited_twice = True
            visited_twice_flag = True

        else:
            visited_twice_flag = False

        if current_node.name == "end":
            if is_small_visited:
                return 1
            return 0

        if not current_node.is_big():
            visited_set.add(current_node.name)
            is_small_visited = True

        result = 0

        for node_neighbor in self.neighbors[current_node.name]:
            result += self._count_paths_helper(node_neighbor, visited_set, is_small_visited, is_visited_twice)

        if not visited_twice_flag:
            visited_set.discard(current_node.name)

        return result

    def count_paths(self) -> int:
        assert "start" in self.neighbors
        assert "end"   in self.neighbors

        return self._count_paths_helper(Node("start"), set(), False, True)

    def count_paths_visit_twice(self) -> int:
        assert "start" in self.neighbors
        assert "end"   in self.neighbors

        return self._count_paths_helper(Node("start"), set(), False, False)

def get_input() -> Graph:
    graph = Graph()

    with open(FILENAME) as file:
        for line in file.readlines():
            node1_name, node2_name = line.strip().split("-")
            node1, node2 = Node(node1_name), Node(node2_name)

            graph.add_edge(node1, node2)

    return graph

def part_1():
    graph = get_input()

    print(f"There are {graph.count_paths()} distinct paths in this cave system")

def part_2():
    graph = get_input()

    print(f"There are {graph.count_paths_visit_twice()} distinct paths in this cave system")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
