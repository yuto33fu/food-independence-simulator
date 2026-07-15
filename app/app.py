"""Streamlit application for the Food Independence Simulator."""

from __future__ import annotations

import streamlit as st

from models.population import Population
from simulation.simulator import Simulator

PROJECT_TITLE = "Food Independence Simulator"
PROJECT_SUBTITLE = "Phase 4"
PROJECT_MESSAGE = "Food Production & Farmland Simulator"


def initialize_app() -> None:

    st.set_page_config(
        page_title=PROJECT_TITLE,
        page_icon="🌾",
        layout="wide",
    )

    st.title(PROJECT_TITLE)
    st.subheader(PROJECT_SUBTITLE)
    st.write(PROJECT_MESSAGE)

    st.markdown("---")

    population = Population(people=21000)

    simulator = Simulator(population)

    requirements = simulator.annual_food_requirements()
    crop_area = simulator.required_crop_area()
    production = simulator.current_crop_production()
    self_sufficiency = simulator.self_sufficiency_rates()
    farmland = simulator.required_farmland()

    col1, col2 = st.columns(2)

    with col1:

        st.header("Population")
        st.metric("People", f"{population.size:,}")

        st.markdown("---")

        st.header("Required Farmland")

        total = 0

        for crop, area in farmland.items():
            total += area
            st.write(f"**{crop}** : {area:.1f} ha")

        st.success(f"Total : {total:.1f} ha")

    with col2:

        st.header("Self Sufficiency")

        for food, rate in self_sufficiency.items():

            st.progress(min(rate / 100, 1.0))

            st.write(f"{food} : {rate:.1f}%")

    st.markdown("---")

    st.header("Production")

    for food in production:

        st.write(
            f"**{food}**"
            f"　Requirement: {requirements[food]:,.0f} kg"
            f"　Production: {production[food]:,.0f} kg"
        )

    st.success("Phase 4 Complete")


if __name__ == "__main__":
    initialize_app()