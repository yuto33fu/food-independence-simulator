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