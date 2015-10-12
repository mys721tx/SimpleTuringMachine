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
                working_cell = working_cell.get_right_cell()
            except cell.CellError:
                break
        string = tape_string + "\n" + head
        return string

    def move_left(self):
        try:
            self._current_cell = self._current_cell.get_left_cell()
        except cell.CellError:
            temp = cell.Cell(self._blank_symbol)
            self._current_cell.set_left_cell(temp)
            temp.set_right_cell(self._current_cell)
            self._current_cell = temp
            self._left_most = self._current_cell

    def move_right(self):
        try:
            self._current_cell = self._current_cell.get_right_cell()
        except cell.CellError:
            temp = cell.Cell(self._blank_symbol)
            self._current_cell.set_right_cell(temp)
            temp.set_left_cell(self._current_cell)
            self._current_cell = temp

    def read(self):
        return self._current_cell.get_data()

    def write(self, value):
        if not value in self._alphabet:
            raise AlphabetError("Symbol not exist in the alphabet.")
        return self._current_cell.set_data(value)
