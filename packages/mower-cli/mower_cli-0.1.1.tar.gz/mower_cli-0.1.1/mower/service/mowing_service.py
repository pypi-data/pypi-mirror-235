from mower.exception.collision_exception import CollisionException
from mower.model.action import Action
from mower.model.lawn import Lawn


class MowingService:
    lawn: Lawn

    def __init__(self, lawn: Lawn) -> None:
        super().__init__()
        self.lawn = lawn

    def run_all_actions(self):
        for mower in self.lawn.mowers:
            self.run_actions(mower)

    def run_actions(self, mower):
        for action in mower.plannedActions:
            if action == Action.FORWARD:
                forward_position = mower.get_forward_position()
                if not self.lawn.is_free(forward_position):
                    raise CollisionException("Two mowers have collided")
                if not self.lawn.is_inside(forward_position):
                    continue
                mower.move_forward()
            else:
                mower.turn(action)
