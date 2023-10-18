"""Core functions for perf_py_pkg."""


def add_one(number: int) -> int:
    """Add one to a number.

    Args:
        number (int): number to add one to.

    Returns:
        int: number + one.
    """
    return number + 1


def about_me(your_name: str) -> str:
    """Return the most important thing about a person.

    Args:
        your_name (str): name of the person.

    Returns:
        str: the name of the person with 'loves python'.
    """
    return f"The wise {your_name} loves Python."


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name: str) -> None:
        """Blah blah blah.

        Args:
            name (str): A string to assign to the `name` instance attribute.
        """
        self.name = name

    def about_self(self) -> str:
        """Return information about an instance created from ExampleClass."""
        return f"I am a very smart {self.name} object."
