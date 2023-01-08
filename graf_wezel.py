from typing import Any


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any = None, index: int = 0):
        self.data = data
        self.index = index

    def __repr__(self):
        return f'{self.data}'