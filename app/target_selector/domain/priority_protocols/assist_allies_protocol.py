from typing import List

from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.protocol_base_decorator import \
    ProtocolBaseDecorator


class AssistAlliesProtocol(ProtocolBaseDecorator):
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        there_is_an_ally = any(
            r.scanned_point.allies > 0 for r in ranked_scanned_points
        )

        if there_is_an_ally:
            ranked_scanned_points = list(
                filter(lambda r: r.scanned_point.allies > 0, ranked_scanned_points)
            )

        return super().protocol_wrapped.rank_points(ranked_scanned_points)
