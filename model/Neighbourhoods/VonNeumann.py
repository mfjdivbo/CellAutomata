from model.Neighbourhoods.NeighbourhoodInterface import NeighborhoodInterface


class VonNeumann(NeighborhoodInterface):

    def _set_prev_neighbour_states(self):
        self._append_neighbour_state(-1, 0)
        self._append_neighbour_state(0, -1)
        self._append_neighbour_state(0, 1)
        self._append_neighbour_state(1, 0)


