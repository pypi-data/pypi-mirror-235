
class Unreachable(RuntimeError):
    """
    An impossible, unreachable part of the code has been reached.

    Use this exception to denote that a certain part of your code
    that shouldn't logically be reachable has indeed been reached.
    Of course, it will never be reached. But if it is, you'll know.
    """
