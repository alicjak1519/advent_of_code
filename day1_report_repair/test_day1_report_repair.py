from assertpy import assertpy

from .day1_report_repair import ReportRepair


def test_example_input_result():
    example_repair = ReportRepair("inputs/day1_example_input.csv")
    assertpy.assert_that(example_repair.find_product_result()).is_equal_to(514579)


def test_input_result():
    example_repair = ReportRepair("inputs/day1_input.csv")
    assertpy.assert_that(example_repair.find_product_result()).is_equal_to(974304)
