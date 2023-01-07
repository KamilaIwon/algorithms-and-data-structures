from typing import Dict, List
from graf_wezel import Vertex
from krawedz import Edge


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]