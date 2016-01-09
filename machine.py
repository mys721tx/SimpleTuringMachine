"""
machine.py: SimpleTuringMacine
"""

import SimpleTuringMachine.tape as tape
import SimpleTuringMachine.exception as exception


class Machine(object):
    """
    Class for machine
    """

    def __init__(self,
                 alphabet,
                 states,
                 initial_state,
                 state_table
                ):
        """
        states is a list for all states, stored internally as a set.
        state_table is a dictionary of tuples.
            The current cell value and machine state forms the index tuples.
            The tuple is a instruction of
                (write_value, move_direction, next_state)
        first element of states is the halt state.
        """

        if isinstance(states, list):
            self._states = set(states)
        else:
            raise ValueError("states must be a list.")

        if initial_state not in self._states:
            raise exception.StateError("Unknown initial state.")

        self._tape = tape.Tape(alphabet)
        self._state = initial_state
        self._halt_state = states[0]
        self._state_table = state_table

    def get_state(self):
        """
        getter for machine state.
        """

        return self._state

    def get_tape(self):
        """
        getter for tape.
        """

        return self._tape

    def load_tape(self, tape_iterable):
        """
        load tape.
        """

        self._tape.load(tape_iterable)

    def run(self):
        """
        execuate instructions until machine halts.
        """

        if self._state is self._halt_state:
            raise exception.HaltedError("Halted.")

        write_value, move_direction, next_state = self._state_table[
            (self._tape.read(), self._state)
        ]

        if next_state not in self._states:
            raise exception.StateError("Unknown state.")

        self._tape.write(write_value)
        self._tape.move(move_direction)
        self._state = next_state
