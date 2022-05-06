from dataclasses import dataclass
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.target_selector.application.compute_new_target.compute_new_target_command import \
    ComputeNewTargetCommand
from app.target_selector.application.compute_new_target.compute_new_target_handler import \
    ComputeNewTargetHandler
from app.target_selector.domain.entities.scanned_point import ScannedPoint
from app.target_selector.domain.priority_protocols.available_decorator_protocol import \
    AvailableDecoratorProtocol

router = APIRouter()


@dataclass
class EnvironmentVisualInformation:
    protocols: List[AvailableDecoratorProtocol]
    scan: List[ScannedPoint]

class Response(BaseModel):
    x: int
    y: int


@router.post("/radar", response_model=Response)
async def compute_target(environment_visual_information: EnvironmentVisualInformation):
    handler = ComputeNewTargetHandler()

    return handler(
        ComputeNewTargetCommand(
            protocols=environment_visual_information.protocols,
            scanned_points=environment_visual_information.scan,
        )
    )


@router.get("/status")
async def status():
    return {"message": "Hello World"}