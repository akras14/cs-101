"""Simple Graph Class"""

from collections import defaultdict
from pprint import pprint

class Graph(object):
    """Simple Graph"""
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def __add_node(self, node):
        """Add new node to Graph"""
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        """Add new edge to node"""
        if from_node not in self.nodes:
            self.__add_node(from_node)
        if to_node not in self.nodes:
            self.__add_node(to_node)
        self.edges[from_node].append((to_node, distance))

    def show(self):
        """Print nodes and edges"""
        pprint(self.nodes)
        pprint(self.edges)
