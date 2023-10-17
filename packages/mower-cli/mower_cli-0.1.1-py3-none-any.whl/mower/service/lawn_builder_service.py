from typing import List

from pydantic import ValidationError

from mower.exception.bad_config_exception import BadConfigException
from mower.model.action import Action
from mower.model.lawn import Lawn
from mower.model.mower import Mower
from mower.model.orientation import Orientation
from mower.model.position import Position


class LawnBuilderService:
    lawn: Lawn

    def __init__(self, config: List[str]):
        last_mower: Mower
        if len(config) < 3:
            raise BadConfigException("The configuration should contain at least 3 lines.")
        for index, line in enumerate(config):
            if index == 0:
                self._init_lawn(line)
            elif index % 2 == 1:
                last_mower = self._init_mower(line)
            else:
                self._init_mower_planned_actions(line, last_mower)

    def _init_lawn(self, line: str):
        pos = line.split()
        try:
            self.lawn = Lawn(upper_right_corner=Position(x=pos[0], y=pos[1]))
        except (IndexError, ValidationError):
            raise BadConfigException("The upper right corner position should be described like this: \"5 4\".")

    def _init_mower(self, line: str) -> Mower:
        pos = line.split()
        try:
            last_mower = Mower(position=Position(x=pos[0], y=pos[1]), orientation=Orientation[pos[2]])
        except (IndexError, KeyError, ValidationError):
            raise BadConfigException("The mower position should be described like this: \"3 3 N\".")
        self.lawn.mowers.append(last_mower)
        return last_mower

    def _init_mower_planned_actions(self, line: str, mower: Mower):
        for char in line:
            try:
                parsed_action = Action(char)
            except ValueError:
                raise BadConfigException("The mower planned actions should be described like this: \"LFLFLFLFF\".")
            mower.plannedActions.append(parsed_action)
