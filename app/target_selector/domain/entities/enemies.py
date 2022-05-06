from dataclasses import dataclass

from app.target_selector.domain.entities.enemy_type import EnemyType


@dataclass
class Enemies:
    type: EnemyType
    number: int

    def __str__(self) -> str:
        return f"Enemies(type={self.type}, number={self.number})"
