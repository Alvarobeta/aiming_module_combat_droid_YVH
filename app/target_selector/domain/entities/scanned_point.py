from dataclasses import dataclass
from typing import Optional

from app.target_selector.domain.entities.coordinates import Coordinates
from app.target_selector.domain.entities.enemies import Enemies


@dataclass
class ScannedPoint:
    coordinates: Coordinates
    enemies: Enemies
    allies: Optional[int] = 0

    def __str__(self) -> str:
        return f"ScannedPoint(coordinates={self.coordinates}, enemies={self.enemies}, allies={self.allies})"
