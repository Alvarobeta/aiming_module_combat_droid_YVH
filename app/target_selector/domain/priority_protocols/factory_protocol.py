from typing import ClassVar, Dict, List

from app.target_selector.domain.priority_protocols.assist_allies_protocol import \
    AssistAlliesProtocol
from app.target_selector.domain.priority_protocols.available_decorator_protocol import \
    AvailableDecoratorProtocol
from app.target_selector.domain.priority_protocols.avoid_crossfire_protocol import \
    AvoidCrossfireProtocol
from app.target_selector.domain.priority_protocols.avoid_mech_protocol import \
    AvoidMechProtocol
from app.target_selector.domain.priority_protocols.closest_enemies_protocol import \
    ClosestEnemiesProtocol
from app.target_selector.domain.priority_protocols.furthest_enemies_protocol import \
    FurthestEnemiesProtocol
from app.target_selector.domain.priority_protocols.incompatible_protocols_exception import \
    IncompatibleProtocolsException
from app.target_selector.domain.priority_protocols.prioritize_mech_protocol import \
    PrioritizeMechProtocol
from app.target_selector.domain.priority_protocols.protocol_interface import \
    ProtocolInterface


class FactoryProtocol:
    PROTOCOL_MAP: ClassVar[Dict] = {
        AvailableDecoratorProtocol.ASSIST_ALLIES: AssistAlliesProtocol,
        AvailableDecoratorProtocol.AVOID_CROSSFIRE: AvoidCrossfireProtocol,
        AvailableDecoratorProtocol.AVOID_MECH: AvoidMechProtocol,
        AvailableDecoratorProtocol.CLOSEST_ENEMIES: ClosestEnemiesProtocol,
        AvailableDecoratorProtocol.FURTHEST_ENEMIES: FurthestEnemiesProtocol,
        AvailableDecoratorProtocol.PRIORITIZE_MECH: PrioritizeMechProtocol,
    }

    INCOMPATIBLE_PROTOCOLS = [
        [
            AvailableDecoratorProtocol.CLOSEST_ENEMIES,
            AvailableDecoratorProtocol.FURTHEST_ENEMIES,
        ],
        [
            AvailableDecoratorProtocol.ASSIST_ALLIES,
            AvailableDecoratorProtocol.AVOID_CROSSFIRE,
        ],
        [
            AvailableDecoratorProtocol.PRIORITIZE_MECH,
            AvailableDecoratorProtocol.AVOID_MECH,
        ],
    ]

    def build(
        self,
        protocol_to_decorate: ProtocolInterface,
        protocols_to_add: List[AvailableDecoratorProtocol],
    ) -> ProtocolInterface:
        for i in self.INCOMPATIBLE_PROTOCOLS:
            if all(t in protocols_to_add for t in i):
                raise IncompatibleProtocolsException()

        for p in protocols_to_add:
            protocol_to_decorate = self.PROTOCOL_MAP[p](protocol_to_decorate)

        return protocol_to_decorate
