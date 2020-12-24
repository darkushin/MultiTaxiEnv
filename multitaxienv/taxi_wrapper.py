# In this file we will implement the taxi wrapper
import networkx as nx

MAP1 = [
    "+---------+",
    "|X: |F: :X|",
    "| : | : : |",
    "| : : : : |",
    "| | : | : |",
    "|X| :G|X: |",
    "+---------+",
]

MAP2 = [
    "+-----------+",
    "|X: |F: :X: |",
    "| : | : : : |",
    "| : : : : : |",
    "| | : | : : |",
    "|X| :G|X: : |",
    "+-----------+",
]


class TaxiMap:
    def __init__(self, desc):
        """
        Args:
            desc: Map description (list of strings)
        """
        self.rows = len(desc) - 2
        self.cols = len(desc[0]) // 2
        self.graph = nx.empty_graph(self.rows * self.cols)
        for i in self.graph.nodes:
            row, col = self.node_to_cors(i)
            # if desc[row][col * 2 + 1] != '-':  # Check north
            #     self.graph.add_edge(i, self.cors_to_node(row - 1, col))
            if desc[row + 2][col * 2 + 1] != '-':  # Check south
                self.graph.add_edge(i, self.cors_to_node(row + 1, col))
            # if desc[row + 1][col * 2] == ':':  # Check west
            #     self.graph.add_edge(i, self.cors_to_node(row, col - 1))
            if desc[row + 1][col * 2 + 2] == ':':  # Check east
                self.graph.add_edge(i, self.cors_to_node(row, col + 1))
        print('hi')

    def node_to_cors(self, node):
        return node // self.cols, node % self.cols

    def cors_to_node(self, row, col):
        return row * self.cols + col

