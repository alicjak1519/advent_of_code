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

    def _set_map_width(self):
        if self.input is None:
            self.map_width = 0
        else:
            self.map_width = len(self.input[0])

    def _set_map_height(self):
        if self.input is None:
            self.map_height = 0
        else:
            self.map_height = len(self.input)

    def _is_tree(self, position):
        lol = self.input[position[0] % self.map_width][position[1]]
        offset = position[0] // self.map_width
        if offset == 0:
            return self.input[position[0]][position[1]] == '#'
        else:
            return self.input[position[0] % self.map_width - offset][position[1]] == '#'

    def _move_actual_position(self, plus_x, plus_y):
        self.actual_position[0] += plus_x
        self.actual_position[1] += plus_y

    def count_trees(self):
        self._set_map_height()
        self._set_map_width()
        tree_number = 0
        while self.actual_position[1] < self.map_height:
            tree_number += self._is_tree(self.actual_position)
            self._move_actual_position(3, 1)

        return tree_number


if __name__ == "__main__":
    toboggan_trajectory = TobogganTrajectory("../inputs/day3_example_input.csv")
    print(toboggan_trajectory.count_trees())
