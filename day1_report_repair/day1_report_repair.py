from functools import reduce
from typing import List, Tuple
from itertools import combinations


class ReportRepair:
    def __init__(self, path: str) -> None:
        self.input = self._read_input(path)

    def _read_input(self, path: str) -> List[int]:
        with open(path) as file:
            return [int(line) for line in file.readlines()]

    def _find_2020_combination(self, number: int) -> Tuple[int]:
        for combination in combinations(self.input, number):
            if reduce(lambda x, y: x + y, combination) == 2020:
                return combination

    def multiply_2020_combination(self, number: int) -> int:
        return reduce(lambda x, y: x * y, self._find_2020_combination(number))


if __name__ == "__main__":
    report_repair = ReportRepair("../inputs/day1_example_input.csv")
    solution_for_two_elements = report_repair.multiply_2020_combination(2)
    solution_for_three_elements = report_repair.multiply_2020_combination(3)
    print(f"Solution for two elements: {solution_for_two_elements}")
    print(f"Solution for three elements: {solution_for_three_elements}")
