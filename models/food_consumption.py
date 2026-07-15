"""
Annual food consumption per person.

All values are expressed in kilograms per person per year.
"""

from dataclasses import dataclass

from models.food_item import FoodItem


@dataclass(frozen=True, slots=True)
class FoodConsumption:
    """
    Represents the annual consumption of a single food item
    for one person.
    """

    food: FoodItem
    kg_per_person_per_year: float