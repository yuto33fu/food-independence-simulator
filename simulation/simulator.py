from models.crop_database import CROPS


class Simulator:

    def __init__(self, population):
        self.population = population

    def annual_food_requirements(self):
        requirements = {}

        for crop in CROPS.values():
            requirements[crop.food.name] = (
                crop.food.per_person * self.population.size
            )

        return requirements

    def required_crop_area(self):
        area = {}

        for crop in CROPS.values():

            amount = crop.food.per_person * self.population.size

            area[crop.food.name] = amount / crop.yield_per_ha

        return area

    def current_crop_production(self):

        production = {}

        for crop in CROPS.values():

            production[crop.food.name] = (
                crop.current_area * crop.yield_per_ha
            )

        return production

    def self_sufficiency_rates(self):

        rate = {}

        production = self.current_crop_production()
        requirement = self.annual_food_requirements()

        for food in requirement:

            rate[food] = (
                production[food] / requirement[food]
            ) * 100

        return rate

    def required_farmland(self):
        return self.required_crop_area()