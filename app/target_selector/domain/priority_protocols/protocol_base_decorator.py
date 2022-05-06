from abc import ABC

from app.target_selector.domain.priority_protocols.protocol_interface import \
    ProtocolInterface


class ProtocolBaseDecorator(ProtocolInterface, ABC):
    def __init__(self, protocol_wrapped: ProtocolInterface = None):
        self._protocol_wrapped = protocol_wrapped

    @property
    def protocol_wrapped(self) -> ProtocolInterface:
        return self._protocol_wrapped

    def __str__(self) -> str:
        return self.__class__.__name__ + "(" + str(self._protocol_wrapped) + ")"
