from functools import reduce
from typing import List


class TobogganTrajectory:
    def __init__(self, path: str) -> None:
        self.input = self._read_input(path)
        self.map_width = 0
        self.map_height = 0
        self.actual_position = [0, 0]

    def _read_input(self, path: str) -> List[str]:
        with open(path) as file:
            return [line.replace('\n', '') for line in file.readlines()]

    def _set_map_width(self) -> None:
        if self.input is None:
            self.map_width = 0
        else:
            self.map_width = len(self.input[0])

    def _set_map_height(self) -> None:
        if self.input is None:
            self.map_height = 0
        else:
            self.map_height = len(self.input)

    def _is_tree(self, position: List[int]) -> bool:
        return self.input[position[1]][position[0] % self.map_width] == '#'

    def _reset_actual_position(self) -> None:
        self.actual_position = [0, 0]

    def _move_actual_position(self, plus_x: int, plus_y: int) -> None:
        self.actual_position[0] += plus_x
        self.actual_position[1] += plus_y

    def count_trees(self, move_x: int, move_y: int) -> int:
        self._set_map_height()
        self._set_map_width()
        self._reset_actual_position()
        tree_number = 0
        while self.actual_position[1] < self.map_height:
            tree_number += self._is_tree(self.actual_position)
            self._move_actual_position(move_x, move_y)
        return tree_number

    def multiply_trees_number(self, moves: List[List[int]]) -> int:
        return reduce(lambda x, y: x * y, [self.count_trees(move[0], move[1]) for move in moves])


if __name__ == "__main__":
    toboggan_trajectory = TobogganTrajectory("../inputs/day3_input.csv")
    print(f"Solution part 1: {toboggan_trajectory.count_trees(3, 1)}")
    print(f"Solution part 2: {toboggan_trajectory.multiply_trees_number([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])}")
