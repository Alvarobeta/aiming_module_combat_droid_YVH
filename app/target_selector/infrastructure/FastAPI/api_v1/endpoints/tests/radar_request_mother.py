import random
from typing import List

from app.target_selector.infrastructure.FastAPI.api_v1.endpoints.tests.point_mother import \
    PointMother


class RadarRequestMother:
    def __init__(self, protocols: List[str] = None, points: List[dict] = None):
        self._protocols = protocols or self._generate_protocols()
        self._points = points or self._generate_points()

    @staticmethod
    def _generate_protocols() -> List[str]:
        protocols = []

        incompatible_protocols = [
            ["closest-enemies", "furthest-enemies"],
            ["assist-allies", "avoid-crossfire"],
            ["prioritize-mech", "avoid-mech"],
        ]

        for i in incompatible_protocols:
            if random.randrange(2):
                protocols.append(random.choice(i))

        return protocols

    @staticmethod
    def _generate_points() -> List[dict]:
        points: [dict] = []

        for _ in range(random.randint(1, 10)):
            points.append(PointMother().build())

        return points

    def add_point(self, point: dict):
        self._points.append(point)

    def build(self) -> dict:
        return {"protocols": self._protocols, "scan": self._points}
