from enum import Enum


class AvailableDecoratorProtocol(str, Enum):
    CLOSEST_ENEMIES = "closest-enemies"
    FURTHEST_ENEMIES = "furthest-enemies"
    ASSIST_ALLIES = "assist-allies"
    AVOID_CROSSFIRE = "avoid-crossfire"
    PRIORITIZE_MECH = "prioritize-mech"
    AVOID_MECH = "avoid-mech"
