# Python Imports
# Third-Party Imports
# Project Imports


class Rectangle:

    def __init__(self, rectangle_code: str, top_x: int, top_y: int, width: int, height: int, local_player: bool):
        self.rectangle_code: str = rectangle_code
        self.top_x: int = top_x
        self.top_y: int = top_y
        self.width: int = width
        self.height: int = height
        self.local_player: bool = local_player

    def is_position_inside_rectangle(self, x, y) -> bool:
        return self.top_x <= x <= self.top_x + self.width and self.top_y >= y >= self.top_y - self.height
