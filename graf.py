from typing import Dict, List, Any, Optional, Callable, Type
from graf_wezel import Vertex
from krawedz import Edge
from typ_krawedzi import EdgeType
from kolejka import Queue
from graphviz import Digraph


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> 'Vertex':
        new = Vertex(data, len(self.adjacencies))
        self.adjacencies[new] = []
        return new

    def add_directed_edge(self,
                          source: 'Vertex',
                          destination: 'Vertex',
                          weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_edge)

    def add_undirected_edge(self,
                            source: 'Vertex',
                            destination: 'Vertex',
                            weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType,
            source: 'Vertex',
            destination: 'Vertex',
            weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def __repr__(self) -> str:
        text = f''
        for key in self.adjacencies.keys():
            text += f'{key.index}:{key.data} ----> {self.adjacencies[key]}\n'

        return text

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        visited = []
        queue = Queue()

        first = list(self.adjacencies.keys())[0]
        queue.enqueue(first)
        visited.append(first)

        while queue.__len__() != 0:
            element = queue.dequeue()
            visit(element)
            for neighbour in self.adjacencies[element]:
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    queue.enqueue(neighbour.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:

        def dfs(neighbour: 'Vertex', visited : List['Vertex'], visit: Callable[[Any], None]):
            visit(neighbour)
            visited.append(neighbour)
            for element in self.adjacencies[neighbour]:
                if element.destination not in visited:
                    visited.append(element.destination)
                    dfs(element.destination, visited, visit)

        visited = []
        first = list(self.adjacencies.keys())[0]
        visit(first)
        visited.append(first)
        for neighbour in self.adjacencies[first]:
            if neighbour.destination not in visited:
                dfs(neighbour.destination, visited, visit)


    def show(self) -> None:

        g = Digraph(format='png')
        # metoda rysujaca krawedz nieskierowana:
        def draw_undirected_edge(graf: 'Digraph', source: 'Vertex',
                                 destination: 'Vertex',
                                 weight: Optional[float] = None):

            if weight:
                graf.edge(str(source.data), str(destination.data), dir='none', label=str(weight))
            else:
                graf.edge(str(source.data), str(destination.data), dir='none')

        # metoda rysujaca krawedz skierowana:

        def draw_directed_edge(graf: 'Digraph', source: 'Vertex',
                                 destination: 'Vertex',
                                 weight: Optional[float]):

            if weight:
                graf.edge(str(source.data), str(destination.data), dir='forward', label=str(weight))
            else:
                graf.edge(str(source.data), str(destination.data), dir='forward')

        # do listy dodajemy wszystkie pary krawedzi:

        li = []
        for x in self.adjacencies.keys():
            for y in self.adjacencies[x]:
                li.append([x, y.destination, y.weight])

        # sprawdzamy czy pojawiaja sie pary odwrotne i rysujemy krawedzie
        done = []
        for z in li:
            if [z[1], z[0], z[2]] in li and \
                    [z[1], z[0]] not in done \
                    and [z[0], z[1]] not in done:
                draw_undirected_edge(g, z[0], z[1], z[2])
                done.append([z[1], z[0]])
                done.append([z[0],z[1]])
            elif [z[1], z[0]] not in done and [z[0], z[1]] not in done:
                draw_directed_edge(g, z[0], z[1], z[2])
        g.view()







