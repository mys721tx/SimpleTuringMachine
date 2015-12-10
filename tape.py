"""
tape.py: Tape module for SimpleTuringMacine
"""

import SimpleTuringMachine.exception as exception
import SimpleTuringMachine.cell as cell

DIRECTION_REVERSE = {
    "L": "R",
    "R": "L"
}

class Tape(object):
    """
    Class for tape
    """

    def __init__(self, alphabet):
        """
        alphabet is a list of symbols used in the tape, stored internally as a set.
        first element of alphabet is the blank symbol.
        """
        if isinstance(alphabet, list):
            self._alphabet = set(alphabet)
        else:
            raise ValueError("alphabet must be a list.")
        self._blank_symbol = alphabet[0]
        self._current_cell = cell.Cell(self._blank_symbol)
        self._left_most = self._current_cell

    def __str__(self):
        """
        String repersentation of Tape object.
        """

        tape_string = ""
        head = ""
        working_cell = self._left_most
        while True:
            if working_cell == self._current_cell:
                head += "^"
            else:
                head += " " * len(str(working_cell.get_data()))
            tape_string += str(working_cell.get_data())
            try:
                working_cell = working_cell.get_neighbor("R")
            except exception.CellError:
                break
        string = tape_string + "\n" + head
        return string

    def move(self, direction):
        """
        Move the current cell to given position.
        If that cell does not exist then create one.
        """

        try:
            self._current_cell = self._current_cell.get_neighbor(direction)
        except exception.CellError:
            temp = cell.Cell(self._blank_symbol)
            self._current_cell.set_neighbor(direction, temp)
            temp.set_neighbor(DIRECTION_REVERSE[direction], self._current_cell)
            self._current_cell = temp
            if direction == "L":
                self._left_most = self._current_cell

    def read(self):
        """
        Read current cell.
        """

        return self._current_cell.get_data()

    def write(self, value):
        """
        Write to current cell.
        """

        if value not in self._alphabet:
            raise exception.AlphabetError("Symbol not exist in the alphabet.")
        return self._current_cell.set_data(value)
