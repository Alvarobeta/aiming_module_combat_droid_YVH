from dataclasses import dataclass

from app.target_selector.domain.entities.scanned_point import ScannedPoint


@dataclass
class RankedScannedPoint:
    scanned_point: ScannedPoint
    rank: float = 0.0

    def __str__(self) -> str:
        return (
            f"RankedScannedPoint(scanned_point={self.scanned_point}, rank={self.rank})"
        )
