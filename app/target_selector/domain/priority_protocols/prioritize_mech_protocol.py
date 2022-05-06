from typing import List

from app.target_selector.domain.entities.enemy_type import EnemyType
from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.protocol_base_decorator import \
    ProtocolBaseDecorator


class PrioritizeMechProtocol(ProtocolBaseDecorator):
    def rank_points(
        self, ranked_scanned_points: List[RankedScannedPoint]
    ) -> List[RankedScannedPoint]:
        there_is_an_mech = any(
            EnemyType.MECH == r.scanned_point.enemies.type
            for r in ranked_scanned_points
        )

        if there_is_an_mech:
            ranked_scanned_points = list(
                filter(
                    lambda r: EnemyType.MECH == r.scanned_point.enemies.type,
                    ranked_scanned_points,
                )
            )

        return super().protocol_wrapped.rank_points(ranked_scanned_points)
