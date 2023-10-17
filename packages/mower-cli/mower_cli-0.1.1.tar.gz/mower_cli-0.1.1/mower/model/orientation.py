from enum import Enum

from mower.model.turn_type import TurnType


class Orientation(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def turn(self, turn_type: TurnType):
        if turn_type == TurnType.RIGHT:
            return Orientation((self.value + 1) % len(Orientation))
        else:
            return Orientation((self.value - 1) % len(Orientation))
