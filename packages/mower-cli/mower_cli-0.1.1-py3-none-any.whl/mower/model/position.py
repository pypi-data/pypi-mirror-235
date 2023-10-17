from pydantic import BaseModel


class Position(BaseModel):
    x: int
    y: int

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def get_short_position(self) -> str:
        return f"{self.x} {self.y}"
