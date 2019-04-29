from model.Cells.Cell import Cell
from model.Cells.CellFactory import CellFactory


class RuleSet:
    dimensions = {
        "1D": 1,
        "2D": 2
    }
    cell_type = Cell
    required_dimension = None
    allow_dead_cells = True

    def __init__(self):
        self.cell_factory = CellFactory(self.get_cell_type())

    def __str__(self):
        return self.__class__.__name__

    def apply(self, previous_state, cell_column):
        pass

    def get_initial_random_state(self, number_of_alive_cells, columns, rows=None):
        pass

    @staticmethod
    def get_cell_type():
        return RuleSet.cell_type

    @staticmethod
    def get_required_dimension():
        return RuleSet.required_dimension

    def get_dead_cell(self):
        return self.cell_type.get_dead_state()

