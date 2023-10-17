from typing import List

from pydantic import BaseModel

from mower.model.mower import Mower
from mower.model.position import Position


class Lawn(BaseModel):
    upper_right_corner: Position
    mowers: List[Mower] = []

    def is_inside(self, position: Position) -> bool:
        return 0 <= position.x <= self.upper_right_corner.x and 0 <= position.y <= self.upper_right_corner.y

    def is_free(self, position: Position) -> bool:
        mower_positions = {m.position for m in self.mowers}
        return position not in mower_positions

    def get_mowers_short_locations(self) -> str:
        separator = '\n'
        return separator.join(list(map(lambda m: m.get_short_location(), self.mowers)))
