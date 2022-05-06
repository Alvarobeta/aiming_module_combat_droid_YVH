from enum import Enum


class EnemyType(str, Enum):
    SOLDIER = "soldier"
    MECH = "mech"

    def __str__(self) -> str:
        return self.value
