from enum import Enum
from typing import Iterable


class Rank(Enum):
    Bronze = (0, 25)
    Silver = (25, 50)
    Gold = (50, 75)
    Platinum = (75, 95)
    Diamond = (95, 99)
    Master = (99, 100)
    Grandmaster = (None, None)

    def __init__(self,
                 lower_percentile: int,
                 upper_percentile: int):
        self._lower_percentile = lower_percentile
        self._upper_percentile = upper_percentile

    def lower_percentile(self):
        return self._lower_percentile

    def upper_percentile(self):
        return self._upper_percentile

    def uses_percentile(self):
        return self._lower_percentile is not None


def percentile_based_ranks() -> Iterable[Rank]:
    """Return an iterable of Rank members that use percentile bounds."""
    return (r for r in Rank if r.uses_percentile())
