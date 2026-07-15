"""Tests for the initial application foundation."""

from __future__ import annotations

from app.main import PROJECT_MESSAGE, PROJECT_SUBTITLE, PROJECT_TITLE, initialize_app


def test_project_constant_exists() -> None:
    """The project title constant should be defined."""
    assert PROJECT_TITLE == "Food Independence Simulator"


def test_application_foundation_is_initialized() -> None:
    """The app initialization function should be available and render the expected content."""
    assert callable(initialize_app)
    assert PROJECT_SUBTITLE == "Phase 0"
    assert PROJECT_MESSAGE == "Project Foundation Initialized"
