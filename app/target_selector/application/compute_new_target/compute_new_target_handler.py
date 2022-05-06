from app.target_selector.application.compute_new_target.compute_new_target_command import \
    ComputeNewTargetCommand
from app.target_selector.domain.entities.scanned_point import Coordinates
from app.target_selector.domain.point_selector_service import \
    PointSelectorService


class ComputeNewTargetHandler:
    def __call__(self, command: ComputeNewTargetCommand) -> Coordinates:
        point_selector = PointSelectorService(protocols=command.protocols)

        return point_selector.get_next_point_to_attack(command.scanned_points)
