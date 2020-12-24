# In this file we will implement the taxi wrapper
import networkx as nx


MAP = [
    "+---------+",
    "|X: |F: :X|",
    "| : | : : |",
    "| : : : : |",
    "| | : | : |",
    "|X| :G|X: |",
    "+---------+",
]


class TaxiMap:
    def __init__(self, desc: list):
        """
        Args:
            desc: Map description (list of strings)
        """
        self.rows = len(desc) - 2
        self.cols = len(desc[0]) // 2
        self.graph = nx.empty_graph(self.rows * self.cols)
        for i in self.graph.nodes:
            row, col = self.node_to_cors(i)
            if desc[row + 2][col * 2 + 1] != '-':  # Check south
                self.graph.add_edge(i, self.cors_to_node(row + 1, col))
                # In case we ever use horizontal barriers
            if desc[row + 1][col * 2 + 2] == ':':  # Check east
                self.graph.add_edge(i, self.cors_to_node(row, col + 1))

    def node_to_cors(self, node) -> (int, int):
        return node // self.cols, node % self.cols

    def cors_to_node(self, row, col) -> int:
        return row * self.cols + col

    def get_path(self, origin: (int, int), target: (int, int)):
        node_origin, node_target = self.cors_to_node(*origin), self.cors_to_node(*target)
        if node_origin == node_target:
            return [origin], []

        path = nx.shortest_path(self.graph, node_origin, node_target)
        cord_path = [self.node_to_cors(node) for node in path]
        actions = []
        for node in range(len(path) - 1):
            delta = path[node + 1] - path[node]
            if delta == -1:  # West
                actions.append(3)
            elif delta == 1:  # East
                actions.append(2)
            elif delta == -self.cols:  # North
                actions.append(1)
            else:  # South
                actions.append(0)
        return cord_path, actions


class Taxi:
    def __init__(self, location):
        self.current_location = location
        # self.destination = destination
        self.path_to_dist = []
        self.path_actions = []
        self.taxi_map = TaxiMap(MAP)

    def compute_path(self, dest: list):
        """
        Given a destination point represented by a list of [row, column], compute the shortest path to the given
        destination from the current location of the taxi.
        :param dest: the destination the taxi should go to.
        """
        cord_path, actions = self.taxi_map.get_path(self.current_location, dest)
        self.path_to_dist = cord_path
        self.path_actions = actions

    def get_next_step(self):
        return 

