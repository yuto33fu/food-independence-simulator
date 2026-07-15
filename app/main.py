"""Compatibility shim for the renamed Phase 0 app entry module."""

from app.app import PROJECT_MESSAGE, PROJECT_SUBTITLE, PROJECT_TITLE, initialize_app

__all__ = ["PROJECT_TITLE", "PROJECT_SUBTITLE", "PROJECT_MESSAGE", "initialize_app"]
