from typing import Optional
from graf_wezel import Vertex


class Edge:
    source: 'Vertex'
    destination: 'Vertex'
    weight: Optional[float]