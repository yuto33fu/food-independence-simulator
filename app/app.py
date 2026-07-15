"""Streamlit application for the Food Independence Simulator."""

from __future__ import annotations

import streamlit as st

from models.population import Population
from simulation.simulator import Simulator

PROJECT_TITLE = "Food Independence Simulator"
PROJECT_SUBTITLE = "Phase 1"
PROJECT_MESSAGE = "Basic Food Requirement Simulator"


def initialize_app() -> None:
    """Render the simulator interface."""
    st.set_page_config(page_title=PROJECT_TITLE, page_icon="🌾")

    st.title(PROJECT_TITLE)
    st.subheader(PROJECT_SUBTITLE)
    st.write(PROJECT_MESSAGE)

    # Default population (Hida City)
    population = Population(people=21000)

    simulator = Simulator(population)
    requirements = simulator.annual_food_requirements()

    st.markdown("---")
    st.header("Annual Food Requirements")

    st.write(f"Population: {population.size:,} people")

    for food, amount in requirements.items():
        st.write(f"**{food}** : {amount:,.0f} kg/year")


if __name__ == "__main__":
    initialize_app()