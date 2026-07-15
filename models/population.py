"""
Population model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Population:
    """
    Represents the population of a region.
    """

    people: int

    @property
    def size(self) -> int:
        """Return the population size."""
        return self.people