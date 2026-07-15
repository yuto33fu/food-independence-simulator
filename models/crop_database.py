"""
Default crop database.
"""

from models.crop import Crop
from models.food_item import (
    RICE,
    VEGETABLE,
    SOYBEAN,
    POTATO,
)

CROP_DATABASE = [
    Crop(
        food=RICE,
        yield_per_hectare=5000,
        cultivated_area=1100,
    ),
    Crop(
        food=VEGETABLE,
        yield_per_hectare=20000,
        cultivated_area=275,
    ),
    Crop(
        food=SOYBEAN,
        yield_per_hectare=2500,
        cultivated_area=50,
    ),
    Crop(
        food=POTATO,
        yield_per_hectare=30000,
        cultivated_area=20,
    ),
]