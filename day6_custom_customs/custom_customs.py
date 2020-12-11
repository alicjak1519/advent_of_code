from typing import List
from collections import Counter


class CustomCustoms:
    def __init__(self, path):
        self.input = self._read_input(path)

    def _read_input(self, path: str) -> List[str]:
        with open(path) as file:
            raw_input = [line for line in file.readlines()]
            input = []
            group = []
            for line in raw_input:
                if line == '\n':
                    input.append(group)
                    group = []
                else:
                    group.append(line.replace('\n', ''))
            input.append(group)
        return input

    def _calc_unique_answers(self, group) -> int:
        return len(set(''.join(group)))

    def _calc_common_yes_answers(self, group):
        people_number = len(group)
        count = Counter(''.join(group))
        return len([key for key in count.keys() if count[key] == people_number])

    def calc_sum_of_unique_answers(self) -> int:
        return sum([self._calc_unique_answers(group) for group in self.input])

    def calc_sum_of_common_yes_answets(self) -> int:
        return sum([self._calc_common_yes_answers(group) for group in self.input])


if __name__ == "__main__":
    custom_customs = CustomCustoms("../inputs/day6_input.csv")
    print(custom_customs.calc_sum_of_unique_answers())
    print(custom_customs.calc_sum_of_common_yes_answets())
