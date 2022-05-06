import random


class PointMother:
    @staticmethod
    def build(
        coordinate_x: int = random.randint(0, 100),
        coordinate_y: int = random.randint(0, 100),
        enemies_type: str = random.choice(["soldier", "mech"]),
        enemies_number: int = random.randint(0, 100),
        allies: int = random.randint(0, 100),
    ):
        return {
            "coordinates": {"x": coordinate_x, "y": coordinate_y},
            "enemies": {"type": enemies_type, "number": enemies_number},
            "allies": allies,
        }
