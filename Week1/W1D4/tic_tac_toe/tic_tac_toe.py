from typing import List

class board:

    _grid: List[List[str]] = [[""]*3]*3

    def __init__(self) -> None:
        pass

    def print(self) -> str:
        res = ""
        for row in self._grid:
            for square in row:
                res += square + "|"