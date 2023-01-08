from typing import Optional
from graf_wezel import Vertex


class Edge:
    source: 'Vertex'
    destination: 'Vertex'
    weight: Optional[float]

    def __init__(self, source: 'Vertex',
                 destination: 'Vertex',
                 weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f'{self.destination}'
