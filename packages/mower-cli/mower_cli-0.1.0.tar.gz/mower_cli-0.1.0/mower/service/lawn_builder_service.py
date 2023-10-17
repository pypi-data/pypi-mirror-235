from typing import List

from mower.model.action import Action
from mower.model.lawn import Lawn
from mower.model.mower import Mower
from mower.model.orientation import Orientation
from mower.model.position import Position


class LawnBuilderService:
    lawn: Lawn

    def __init__(self, config: List[str]):
        last_mower: Mower
        for index, line in enumerate(config):
            if index == 0:
                self._init_lawn(line)
            elif index % 2 == 1:
                last_mower = self._init_mower(line)
            else:
                self._init_mower_planned_actions(line, last_mower)

    def _init_lawn(self, line: str):
        pos = line.split()
        self.lawn = Lawn(upper_right_corner=Position(x=pos[0], y=pos[1]))

    def _init_mower(self, line: str) -> Mower:
        pos = line.split()
        last_mower = Mower(position=Position(x=pos[0], y=pos[1]), orientation=Orientation[pos[2]])
        self.lawn.mowers.append(last_mower)
        return last_mower

    def _init_mower_planned_actions(self, line: str, mower: Mower):
        for char in line:
            mower.plannedActions.append(Action(char))
