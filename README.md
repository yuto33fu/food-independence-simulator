# Food Independence Simulator

## Overview

Food Independence Simulator is a long-term scientific simulation project aimed at exploring whether Japan can sustain food supply through domestic resources if imports are interrupted.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running

```bash
pytest
streamlit run app/main.py
```

## Development philosophy

This phase focuses on a clean, testable, and expandable foundation. The project intentionally avoids simulation logic, agricultural models, and other domain-specific calculations at this stage.
