"""
machine.py: SimpleTuringMacine
"""

import tape

ALPHABET = set([0, 1])
BLANK_SYMBOL = 0
STATES = set(["A", "B", "C", "HALT"])
INITIAL_STATE = "A"
HALT_STATE = "HALT"
STATE_TABLE = {
    0:{
        "A": (1, "R", "B"),
        "B": (1, "L", "A"),
        "C": (1, "L", "B")
    },
    1:{
        "A": (1, "L", "C"),
        "B": (1, "R", "B"),
        "C": (1, "R", "HALT")
    }
}

class Error(Exception):
    """
    Base class for exceptions in this module
    """
    pass

class StateError(Error):
    """
    Exception raised for unknown state.
    """
    pass

class HaltedError(Error):
    """
    Exception raised for halted machine.
    """
    pass

class Machine(object):
    """
    Class for machine
    """
    
    def __init__(self, 
        alphabet = ALPHABET, 
        blank_symbol = BLANK_SYMBOL,
        states = STATES,
        initial_state = INITIAL_STATE,
        halt_state = HALT_STATE,
        state_table = STATE_TABLE
        ):
        if not initial_state in states:
            raise StateError("Unknown initial state.")
        if not halt_state in states:
            raise StateError("Unknown halt state.")
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
        MOVE = {
            "L": self._tape.move_left,
            "R": self._tape.move_right
        }
        if self._state == self._halt_state:
            raise HaltedError("Halted.")
        instruction = self._state_table[self._tape.read()][self._state]
        self._tape.write(instruction[0])
        MOVE[instruction[1]]()
        if not instruction[2] in states:
            raise StateError("Unknown state.")
        self._state = instruction[2]
