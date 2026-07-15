"""
Simulation engine.
"""

from models.food_database import FOOD_DATABASE
from models.population import Population


class Simulator:
    """
    Calculates annual food requirements for a population.
    """

    def __init__(self, population: Population) -> None:
        self.population = population

    def annual_food_requirements(self) -> dict[str, float]:
        """
        Returns the annual food requirement (kg/year)
        for each food item.
        """
        requirements: dict[str, float] = {}

        for consumption in FOOD_DATABASE:
            requirements[consumption.food.name] = (
                consumption.kg_per_person_per_year
                * self.population.size
            )

        return requirements
"""Simulation engine."""

from models.crop_database import CROP_DATABASE
from models.food_database import FOOD_DATABASE
from models.population import Population


class Simulator:
    """Calculates food requirements, crop area and production."""

    def __init__(self, population: Population) -> None:
        self.population = population

    def annual_food_requirements(self) -> dict[str, float]:
        requirements: dict[str, float] = {}

        for consumption in FOOD_DATABASE:
            requirements[consumption.food.name] = (
                consumption.kg_per_person_per_year * self.population.size
            )

        return requirements

    def required_crop_area(self) -> dict[str, float]:
        requirements = self.annual_food_requirements()
        result: dict[str, float] = {}

        for crop in CROP_DATABASE:
            food = crop.food.name
            if food in requirements:
                result[food] = crop.required_area(requirements[food])

        return result

    def current_crop_production(self) -> dict[str, float]:
        result: dict[str, float] = {}

        for crop in CROP_DATABASE:
            result[crop.food.name] = crop.annual_production

        return result

    def self_sufficiency_rates(self) -> dict[str, float]:
        requirements = self.annual_food_requirements()
        result: dict[str, float] = {}

        for crop in CROP_DATABASE:
            food = crop.food.name
            if food in requirements:
                result[food] = crop.self_sufficiency_rate(requirements[food])

        return result