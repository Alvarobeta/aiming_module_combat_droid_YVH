import math
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Coordinates:
    x: int
    y: int

    MAX_DISTANCE: ClassVar[float] = 100.0

    def distance_euclidean_to_point_zero_zero(self) -> float:
        return math.dist((self.x, self.y), (0, 0))

    def __str__(self) -> str:
        return f"Coordinates(x={self.x}, y={self.y})"
