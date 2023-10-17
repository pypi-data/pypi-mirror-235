from enum import Enum


class Action(str, Enum):
    TURN_RIGHT = "R"
    TURN_LEFT = "L"
    FORWARD = "F"
