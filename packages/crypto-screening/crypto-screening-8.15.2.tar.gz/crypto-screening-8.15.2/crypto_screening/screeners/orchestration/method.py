# method.py

from enum import Enum

__all__ = [
    "OrchestrationMethod"
]

class OrchestrationMethod(Enum):
    """A class to represent an enum of an orchestration method."""

    INDIVIDUALS = "individuals"
    EXCHANGES = "exchanges"
    CATEGORIES = "categories"
    CATEGORIES_EXCHANGES = "categories_exchanges"
    ALL = "all"
# end OrchestrationMethod