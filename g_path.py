from graf import Graph
from kolejka import Queue
from graf_wezel import Vertex
from typing import Dict


class GraphPath:
    graf: 'Graph'
    start: 'Vertex'
    end: 'Vertex'

    def __init__(self,
                 graf: 'Graph',
                 start: 'Vertex',
                 end: 'Vertex') -> None:
        self.graf = graf
        self.start = start
        self.end = end

    def draw_path(self):
        for edge in self.graf.adjacencies.values():
            for x in edge:
                if x.weight:
                    return self._algorytm_dijksry()
        return self._droga_w_niewazonym()

    def _algorytm_dijksry(self):
        # Inicjalizacja tablicy kosztów i tablicy rodziców dla końcowego wierzchołka grafu.
        # Wartość float('inf') oznacza, że koszt przejścia do wierzchołka jest nieznany.
        tablica_kosztow: Dict[Vertex, int] = {self.end: float('inf')}
        tablica_rodzicow: Dict[Vertex, int] = {self.end: None}
        odwiedzony = []

        # Inicjalizacja tablicy kosztów i tablicy rodziców dla sąsiadów początkowego wierzchołka grafu
        for wierzcholek in self.graf.adjacencies[self.start]:
            tablica_kosztow[wierzcholek.destination] = wierzcholek.weight
            tablica_rodzicow[wierzcholek.destination] = self.start

        # Pętla główna algorytmu Dijkstry
        # Zmienne v i c będą przechowywać informację o wierzchołku i jego koszcie odpowiednio.
        v = min(tablica_kosztow, key=tablica_kosztow.get)
        while v:
            c = tablica_kosztow.get(v)
            # Dodanie wierzchołka do listy odwiedzonych
            odwiedzony.append(v)
            for sasiad in self.graf.adjacencies[v]:
                # Jeśli wierzchołek już był odwiedzony, pomiń go.
                if sasiad.destination in odwiedzony:
                    continue
                # Obliczenie nowego kosztu przejścia do sąsiada
                nc = c + sasiad.weight
                # Jeśli sąsiad nie był jeszcze rozpatrywany, ustaw jego rodzica i koszt przejścia.
                if not sasiad.destination in tablica_rodzicow:
                    tablica_rodzicow[sasiad.destination] = v
                    tablica_kosztow[sasiad.destination] = tablica_kosztow[v] + sasiad.weight
                # Jeśli sąsiad był już rozpatrywany, sprawdź, czy obecna droga jest krótsza niż dotychczasowa.
                else:
                    # Jeśli tak, zaktualizuj koszt przejścia i rodzica sąsiada.
                    if nc < tablica_kosztow[sasiad.destination]:
                        tablica_kosztow[sasiad.destination] = nc
                        tablica_rodzicow[sasiad.destination] = v

            # Wybierz następny wierzchołek do przetworzenia - taki, który nie był jeszcze odwiedzony,
            # a ma najniższy koszt przejścia.
            bez_odwiedzonych = dict()
            for wierzcholek, waga in tablica_kosztow.items():
                if wierzcholek not in odwiedzony:
                    bez_odwiedzonych[wierzcholek] = waga
            # Jeśli nie ma już nieodwiedzonych wierzchołków, zakończ pętlę.
            if not bez_odwiedzonych:
                break
            v = min(bez_odwiedzonych, key=bez_odwiedzonych.get)

        # Wyznaczanie najkrótszej ścieżki do końcowego wierzchołka.
        node = self.end

        droga = [str(node.data)]
        while node is not self.start:
            node = tablica_rodzicow[node]
            droga.insert(0, str(node.data))


        return f'droga: {droga}, \nkoszt: {tablica_kosztow[self.end]}'

    def _droga_w_niewazonym(self):

        queue = Queue()
        queue.enqueue([self.start]) # Dodajemy do kolejki sciezki z wierzchołkiem startowym
        visited = list() #lista odwiedzonych elementow
        visited.append(self.start)

        while queue.__len__() != 0:
            p = queue.dequeue() #pobrany element z kolejki to sciezka
            v = p[len(p)-1] #v to ostatni wierzcholek sciezki

            # jezeli wierzcholek to jest to czego szukamy to konczymy program
            if v == self.end:
                return p

            # patrzymy czy wierzcholek jest polaczony z jakims nieodwiedzonym
            for n in self.graf.adjacencies[v]:
                if n.destination not in visited:
                    # jezeli tak to to obecnej sciezki dodajemy ten nieodwiedzony wierzcholek
                    np = list(p)
                    np.append(n.destination)
                    visited.append(n.destination) #ustawiamy go jako odwiedzonego
                    queue.enqueue(np) #dodajemy sciezke do kolejki
