"""
tape.py: Tape module for SimpleTuringMacine
"""

import collections
import SimpleTuringMachine.exception as exception


class Tape(object):
    """
    Class for tape
    """

    def __init__(self, alphabet):
        """
        alphabet is a list of symbols used in the tape,
            stored internally as a set.
        first element of alphabet is the blank symbol.
        """

        if isinstance(alphabet, list):
            self._alphabet = set(alphabet)
        else:
            raise ValueError("alphabet must be a list.")

        self._blank_symbol = alphabet[0]
        self._queue = collections.deque([self._blank_symbol])
        self._current_cell = 0

    def __str__(self):
        """
        String repersentation of Tape object.
        """

        if __debug__:
            tape_string = ""
            head_string = ""
            for index, value in enumerate(self._queue):
                symbol_string = str(value)
                tape_string += symbol_string
                if index == self._current_cell:
                    head_string += "^" + " " * (len(symbol_string) - 1)
                else:
                    head_string += " " * len(symbol_string)
            display_string = tape_string + "\n" + head_string
        else:
            display_string = "".join(str(cell) for cell in self._queue)

        return display_string

    def move(self, direction):
        """
        Move the current cell to given position.
            True is left.
            False is right.
        If that cell does not exist then create one.
        """

        if isinstance(direction, bool):
            if direction:
                if self._current_cell == 0:
                    self._queue.appendleft(self._blank_symbol)
                else:
                    self._current_cell -= 1
            else:
                self._current_cell += 1
                if self._current_cell == len(self._queue):
                    self._queue.append(self._blank_symbol)
        else:
            raise ValueError("Direction must be a bool.")

    def load(self, tape_iterable):
        """
        load tape from a iterable.
        """

        if set(tape_iterable) >= self._alphabet:
            raise exception.AlphabetError("Tape contains unknown symbols.")
        else:
            self._queue = collections.deque(tape_iterable)

    def read(self):
        """
        Read current cell.
        """

        return self._queue[self._current_cell]

    def write(self, value):
        """
        Write to current cell.
        """

        if value not in self._alphabet:
            raise exception.AlphabetError("Symbol not exist in the alphabet.")
        else:
            self._queue[self._current_cell] = value
