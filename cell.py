"""
cell.py: Cell module for SimpleTuringMacine
"""

# Translate to full directions
DIRECTIONS = {
    "L": "Left",
    "R": "Right"
}

class Error(Exception):
    """
    Base class for exceptions in this module
    """
    pass

class CellError(Error):
    """
    Exception raised for none-existing cell
    """
    pass

class Cell(object):
    """
    Class for cell in a tape
    """

    def __init__(self, data = None, left_neighbor = None, right_neighbor = None):
        self._data = data
        self._neighbors = {
            "L": left_neighbor,
            "R": right_neighbor
        }

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_neighbor(self, direction):
        if self._neighbors[direction] == None:
            raise CellError("%s cell does not exist." % DIRECTIONS[direction])
        return self._neighbors[direction]

    def set_neighbor(self, direction, neighbor):
        self._neighbors[direction] = neighbor
