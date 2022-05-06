from dataclasses import dataclass
from typing import List

from app.target_selector.domain.entities.scanned_point import ScannedPoint
from app.target_selector.domain.priority_protocols.available_decorator_protocol import \
    AvailableDecoratorProtocol


@dataclass
class ComputeNewTargetCommand:
    protocols: List[AvailableDecoratorProtocol]
    scanned_points: List[ScannedPoint]
