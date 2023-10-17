from typing import List

from pydantic import BaseModel

from mower.model.action import Action
from mower.model.orientation import Orientation
from mower.model.position import Position
from mower.model.turn_type import TurnType

MOVE_DICT = {
    Orientation.N: Position(x=0, y=1),
    Orientation.E: Position(x=1, y=0),
    Orientation.S: Position(x=0, y=-1),
    Orientation.W: Position(x=-1, y=0)
}


class Mower(BaseModel):
    position: Position
    orientation: Orientation
    plannedActions: List[Action] = []

    def get_forward_position(self) -> Position:
        return self.position.model_copy() + MOVE_DICT[self.orientation]

    def move_forward(self):
        self.position = self.get_forward_position()

    def turn(self, turn_type: TurnType):
        self.orientation = self.orientation.turn(turn_type)

    def get_short_location(self) -> str:
        return f"{self.position.get_short_position()} {self.orientation.name}"
