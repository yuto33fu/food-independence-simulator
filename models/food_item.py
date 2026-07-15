"""
Food item definitions for the Food Independence Simulator.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FoodItem:
    """
    Represents a food item used throughout the simulator.
    """

    name: str

    def __str__(self) -> str:
        return self.name


# ==========================================================
# Standard Food Items
# ==========================================================

RICE = FoodItem("Rice")
VEGETABLE = FoodItem("Vegetable")
BEEF = FoodItem("Beef")
PORK = FoodItem("Pork")
CHICKEN = FoodItem("Chicken")
EGG = FoodItem("Egg")
MILK = FoodItem("Milk")
SOYBEAN = FoodItem("Soybean")
POTATO = FoodItem("Potato")