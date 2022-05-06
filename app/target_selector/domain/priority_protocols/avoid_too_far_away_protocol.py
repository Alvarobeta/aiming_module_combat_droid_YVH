from typing import List

from app.target_selector.domain.entities.coordinates import Coordinates
from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.protocol_interface import \
    ProtocolInterface


class AvoidTooFarAwayProtocol(ProtocolInterface):
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        ranked_scanned_points = list(
            filter(
                lambda r: Coordinates.MAX_DISTANCE
                >= r.scanned_point.coordinates.distance_euclidean_to_point_zero_zero(),
                ranked_scanned_points,
            )
        )

        return ranked_scanned_points

    def __str__(self) -> str:
        return self.__class__.__name__
