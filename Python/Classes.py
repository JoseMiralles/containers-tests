from typing import List

class AngryBird:

    __slots__ = ["_x", "_y"] # Reserves memory for faster class creation

    def __init__(self, x: int = 0, y: int = 0):
        self._x: int = x
        self._y: int = y

    def move_up_by(self, delta: int):
        self._y += delta

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        if value < 0:
            value = 0
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        if value < 0:
            value = 0
        self._y = value

    def __repr__(self) -> str:
        return f"<AngryBird (X:{self._x}, y:{self._y}))>"
    

bird = AngryBird()
bird2 = AngryBird(x=2, y=4)
print(bird.x)
bird.x = -20 # Will set it to 0 because of setter
bird.move_up_by(10)
print(bird)


# INHERITANCE

class Employee:
    def __init__(self, id: str) -> None:
        self._id = id

class Manager(Employee):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.employees: List[str] = []

    def add_direct_report(self, employee_id: str) -> None:
        self.employees.append(employee_id)
