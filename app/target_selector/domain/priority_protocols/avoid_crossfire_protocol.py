from typing import List

from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.protocol_base_decorator import \
    ProtocolBaseDecorator


class AvoidCrossfireProtocol(ProtocolBaseDecorator):
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        ranked_scanned_points = list(
            filter(lambda r: not r.scanned_point.allies, ranked_scanned_points)
        )

        return super().protocol_wrapped.rank_points(ranked_scanned_points)
