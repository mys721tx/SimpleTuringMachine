"""
cell.py: Cell module for SimpleTuringMacine
"""

import SimpleTuringMachine.exception as exception

# Translate to full directions
DIRECTIONS = {
    "L": "Left",
    "R": "Right"
}

class Cell(object):
    """
    Class for cell in a tape
    """

    def __init__(self, data=None, left_neighbor=None, right_neighbor=None):
        """
        __init__ method
        """

        self._data = data
        self._neighbors = {
            "L": left_neighbor,
            "R": right_neighbor
        }

    def get_data(self):
        """
        getter for self._data
        """

        return self._data

    def set_data(self, data):
        """
        getter for self._data
        """

        self._data = data

    def get_neighbor(self, direction):
        """
        getter for neighbor Cell object
        """

        if self._neighbors[direction] is None:
            raise exception.CellError("%s cell does not exist." % DIRECTIONS[direction])
        return self._neighbors[direction]

    def set_neighbor(self, direction, neighbor):
        """
        setter for neighbor Cell object
        """

        self._neighbors[direction] = neighbor
