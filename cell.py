"""
cell.py: Cell module for SimpleTuringMacine
"""

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

class Cell():
    """
    Class for cell in a tape
    """

    def __init__(self, data = None, left_cell = None, right_cell = None):
        self._data = data
        self._left_cell = left_cell
        self._right_cell = right_cell

    def get_data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data
        
    def get_left_cell(self):
        if self._left_cell == None:
            raise CellError("Left cell does not exist.")
        return self._left_cell

    def get_right_cell(self):
        if self._right_cell == None:
            raise CellError("Right cell does not exist.")
        return self._right_cell

    def set_left_cell(self, left_cell):
        self._left_cell = left_cell

    def set_right_cell(self, right_cell):
        self._right_cell = right_cell
