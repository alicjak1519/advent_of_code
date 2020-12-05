from assertpy import assertpy

from .binary_boarding import BinaryBoarding

binary_boarding = BinaryBoarding("inputs/day5_example_input.csv")


def test_example_input_result_part1():
    assertpy.assert_that(binary_boarding.find_highest_id()).is_equal_to(820)
