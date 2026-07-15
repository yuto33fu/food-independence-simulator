"""
Default annual food consumption database.

Values are approximate kilograms per person per year.
"""

from models.food_consumption import FoodConsumption
from models.food_item import (
    RICE,
    VEGETABLE,
    BEEF,
    PORK,
    CHICKEN,
    EGG,
    MILK,
    SOYBEAN,
    POTATO,
)

FOOD_DATABASE = [
    FoodConsumption(RICE, 50.0),
    FoodConsumption(VEGETABLE, 100.0),
    FoodConsumption(BEEF, 6.0),
    FoodConsumption(PORK, 13.0),
    FoodConsumption(CHICKEN, 14.0),
    FoodConsumption(EGG, 17.0),
    FoodConsumption(MILK, 60.0),
    FoodConsumption(SOYBEAN, 8.0),
    FoodConsumption(POTATO, 18.0),
]