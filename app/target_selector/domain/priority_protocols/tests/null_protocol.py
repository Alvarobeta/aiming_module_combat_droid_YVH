from typing import List

from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.protocol_interface import \
    ProtocolInterface


class NullProtocol(ProtocolInterface):
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        return ranked_scanned_points

    def __str__(self) -> str:
        return self.__class__.__name__
