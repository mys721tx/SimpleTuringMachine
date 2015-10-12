"""
machine.py: SimpleTuringMacine
"""

import tape
import exception

class Machine(object):
    """
    Class for machine
    """

    def __init__(self,
        alphabet = set(),
        blank_symbol = None,
        states = set(),
        initial_state = None,
        halt_state = None,
        state_table = dict()
        ):
        """
        states is a set for all states
        state_table is a dictionary of dictionaries of tuples.
            Key for the first layer dictionary is the symbol read on tape.
            Key for the second layer dictionary is the current state.
            The tuple is a instruction of
                (write_value, tape_direction, next_state)
        """
        if not initial_state in states:
            raise exception.StateError("Unknown initial state.")
        if not halt_state in states:
            raise exception.StateError("Unknown halt state.")
        self._tape = tape.Tape(alphabet, blank_symbol)
        self._states = states
        self._state = initial_state
        self._halt_state = halt_state
        self._state_table = state_table

    def get_state(self):
        return self._state

    def get_tape(self):
        return self._tape

    def run(self):
        if self._state == self._halt_state:
            raise exception.HaltedError("Halted.")
        instruction = self._state_table[self._tape.read()][self._state]
        self._tape.write(instruction[0])
        self._tape.move(instruction[1])
        if not instruction[2] in self._states:
            raise exception.StateError("Unknown state.")
        self._state = instruction[2]
