"""
tape.py: Tape module for SimpleTuringMacine
"""

import cell

class Error(Exception):
    """
    Base class for exceptions in this module
    """
    pass

class AlphabetError(Error):
    """
    Exception raised for symbol not exist in the alphabet.
    """
    pass

class Tape(object):
    """
    Class for tape
    """

    def __init__(self, alphabet = None, blank_symbol = None):
        """
        alphabet is a set of symbols used in the tape.
        blank_symbol is the symbol used as blank symbol.
        """
        self._alphabet = alphabet
        if not blank_symbol in self._alphabet:
            raise AlphabetError("Symbol not exist in the alphabet.")
        self._blank_symbol = blank_symbol
        self._current_cell = cell.Cell(self._blank_symbol)
        self._left_most = self._current_cell

    def __str__(self):
        tape_string = ""
        head = ""
        working_cell = self._left_most
        is_head_print = False
        while True:
            if is_head_print:
                head += " "
            elif working_cell == self._current_cell:
                head += "^"
                is_head_print = True
            else:
                head += " "
            tape_string += str(working_cell.get_data())
            try:
                working_cell = working_cell.get_neighbor("R")
            except cell.CellError:
                break
        string = tape_string + "\n" + head
        return string

    def move(self, direction):

        DIRECTION_REVERSE = {
            "L": "R",
            "R": "L"
        }

        try:
            self._current_cell = self._current_cell.get_neighbor(direction)
        except cell.CellError:
            temp = cell.Cell(self._blank_symbol)
            self._current_cell.set_neighbor(direction, temp)
            temp.set_neighbor(DIRECTION_REVERSE[direction], self._current_cell)
            self._current_cell = temp
            if direction == "L":
                self._left_most = self._current_cell

    def read(self):
        return self._current_cell.get_data()

    def write(self, value):
        if not value in self._alphabet:
            raise AlphabetError("Symbol not exist in the alphabet.")
        return self._current_cell.set_data(value)
