from assertpy import assertpy

from .report_repair import ReportRepair

example_repair = ReportRepair("inputs/day1_example_input.csv")


def test_example_input_result():
    assertpy.assert_that(example_repair.multiply_2020_combination(2)).is_equal_to(514579)
