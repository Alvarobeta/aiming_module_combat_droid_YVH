import random

from app.target_selector.domain.entities.coordinates import Coordinates
from app.target_selector.domain.entities.enemies import Enemies
from app.target_selector.domain.entities.enemy_type import EnemyType
from app.target_selector.domain.entities.scanned_point import ScannedPoint


class ScannedPointMother:
    @staticmethod
    def build(
        coordinate_x: int = random.randint(0, 100),
        coordinate_y: int = random.randint(0, 100),
        enemies_type: EnemyType = random.choice(list(EnemyType)),
        enemies_number: int = random.randint(0, 100),
        allies: int = random.randint(0, 100),
    ):

        return ScannedPoint(
            coordinates=Coordinates(x=coordinate_x, y=coordinate_y),
            enemies=Enemies(type=enemies_type, number=enemies_number),
            allies=allies,
        )
