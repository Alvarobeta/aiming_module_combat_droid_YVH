from typing import List

from app.target_selector.domain.entities.coordinates import Coordinates
from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.protocol_base_decorator import \
    ProtocolBaseDecorator


class ClosestEnemiesProtocol(ProtocolBaseDecorator):
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        for r in ranked_scanned_points:
            if r.scanned_point.enemies.number:
                r.rank += (
                    Coordinates.MAX_DISTANCE
                    - r.scanned_point.coordinates.distance_euclidean_to_point_zero_zero()
                )

        return super().protocol_wrapped.rank_points(ranked_scanned_points)
