from math import ceil
from typing import List


class BinaryBoarding:
    def __init__(self, path):
        self.input = self._read_input(path)

    def _read_input(self, path):
        with open(path) as file:
            return [line.replace('\n', '') for line in file.readlines()]

    def _find_row(self, row_code: str) -> int:
        available_row_numbers = list(range(127))
        while len(available_row_numbers) != 1:
            fracture = ceil(len(available_row_numbers) / 2)
            if row_code[0] == 'F':
                available_row_numbers = available_row_numbers[:fracture]
            else:
                available_row_numbers = available_row_numbers[fracture:]
            row_code = row_code[1:]
        return available_row_numbers[0]

    def _find_col(self, col_code: str) -> int:
        available_col_numbers = list(range(8))
        while len(available_col_numbers) != 1:
            fracture = ceil(len(available_col_numbers) / 2)
            if col_code[0] == 'L':
                available_col_numbers = available_col_numbers[:fracture]
            else:
                available_col_numbers = available_col_numbers[fracture:]
            col_code = col_code[1:]
        return available_col_numbers[0]

    def _find_id(self, boarding_pass: str) -> int:
        if len(boarding_pass) == 10:
            return self._find_row(boarding_pass[:7]) * 8 + self._find_col(boarding_pass[-3:])

    def find_highest_id(self) -> int:
        return max([self._find_id(boarding_pass) for boarding_pass in self.input])

    def find_my_seat(self) -> List[int]:
        seated_id_list = [self._find_id(boarding_pass) for boarding_pass in self.input]
        all_available_seats = list(range(8, 933))
        [all_available_seats.remove(seat) for seat in seated_id_list if seat in all_available_seats]
        return all_available_seats


if __name__ == "__main__":
    binary_boarding = BinaryBoarding("../inputs/day5_input.csv")
    print(binary_boarding.find_highest_id())
    print(binary_boarding.find_my_seat())
