"""
Crop model.
"""

from dataclasses import dataclass

from models.food_item import FoodItem


@dataclass(slots=True)
class Crop:
    """
    Represents one agricultural crop.
    """

    food: FoodItem

    yield_per_hectare: float
    """
    Annual yield (kg/ha)
    """

    cultivated_area: float = 0.0
    """
    Current cultivated area (ha)
    """

    @property
    def annual_production(self) -> float:
        """
        Current annual production (kg)
        """
        return self.yield_per_hectare * self.cultivated_area

    def required_area(self, required_kg: float) -> float:
        """
        Area required to produce the requested amount.
        """
        return required_kg / self.yield_per_hectare

    def self_sufficiency_rate(self, required_kg: float) -> float:
        """
        Self-sufficiency rate (%)
        """
        if required_kg == 0:
            return 0.0

        return self.annual_production / required_kg * 100