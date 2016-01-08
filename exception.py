"""
exception.py: Exception module for SimpleTuringMacine
"""

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
