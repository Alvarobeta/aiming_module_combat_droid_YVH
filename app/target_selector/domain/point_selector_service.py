import logging
from typing import List

from app.target_selector.domain.entities.coordinates import Coordinates
from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.entities.scanned_point import ScannedPoint
from app.target_selector.domain.priority_protocols.available_decorator_protocol import \
    AvailableDecoratorProtocol
from app.target_selector.domain.priority_protocols.avoid_too_far_away_protocol import \
    AvoidTooFarAwayProtocol
from app.target_selector.domain.priority_protocols.factory_protocol import \
    FactoryProtocol
from app.target_selector.domain.priority_protocols.protocol_interface import \
    ProtocolInterface

logger = logging.getLogger(__name__)


class PointSelectorService:
    def __init__(self, protocols: List[AvailableDecoratorProtocol]):
        self._factory_protocol = FactoryProtocol()
        self._protocol = self._build_protocol(protocols)

    def _build_protocol(
        self, protocols: List[AvailableDecoratorProtocol]
    ) -> ProtocolInterface:
        protocol: ProtocolInterface = AvoidTooFarAwayProtocol()
        return self._factory_protocol.build(
            protocol_to_decorate=protocol, protocols_to_add=protocols
        )

    def get_next_point_to_attack(
        self, scanned_points: List[ScannedPoint]
    ) -> Coordinates:
        ranked_scanned_points: List[RankedScannedPoint] = [
            RankedScannedPoint(scanned_point=s) for s in scanned_points
        ]

        ranked_scanned_points = self._protocol.rank_points(ranked_scanned_points)

        ranked_points = sorted(
            ranked_scanned_points, key=lambda r: r.rank, reverse=True
        )

        logger.debug(
            f"Ranked points. protocol={self._protocol}, sorted_points={ranked_points}"
        )

        first_ranked_scanned_point: RankedScannedPoint = ranked_points.pop(0)

        return first_ranked_scanned_point.scanned_point.coordinates
