from abc import ABC, abstractmethod
from typing import List

from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint


class ProtocolInterface(ABC):
    @abstractmethod
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
