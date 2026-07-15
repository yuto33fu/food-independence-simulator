"""
Crop model.
"""

from dataclasses import dataclass

from models.food_item import FoodItem


@dataclass(slots=True)
class Crop:
    """
    Represents an agricultural crop.
    """

    food: FoodItem

    yield_per_hectare: float
    """
    Annual yield (kg/ha).
    """

    cultivated_area: float = 0.0
    """
    Current cultivated area (ha).
    """

    @property
    def annual_production(self) -> float:
        """
        Total annual production (kg).
        """
        return self.yield_per_hectare * self.cultivated_area