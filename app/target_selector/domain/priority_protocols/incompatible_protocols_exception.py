from app.target_selector.domain.domain_exception import DomainException


class IncompatibleProtocolsException(DomainException):
    def __init__(self):
        super().__init__(
            type="invalid_combination_of_protocols",
            message="The protocol combination used is not valid.",
            status=422,
        )
