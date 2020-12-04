from assertpy import assertpy

from .toboggan_trajectory import TobogganTrajectory

toboggan_trajectory = TobogganTrajectory("inputs/day3_example_input.csv")


def test_example_input_result_part1():
    assertpy.assert_that(toboggan_trajectory.count_trees(3, 1)).is_equal_to(7)


def test_example_input_result_part2():
    assertpy.assert_that(
        toboggan_trajectory.multiply_trees_number([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])).is_equal_to(336)
