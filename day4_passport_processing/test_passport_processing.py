from assertpy import assertpy

from .passport_processing import PassportProccessing

passport_processing = PassportProccessing("inputs/day4_example_input.csv")
passport_processing_valid = PassportProccessing("inputs/day4_valid_input.csv")
passport_processing_invalid = PassportProccessing("inputs/day4_invalid_input.csv")


def test_example_input_result_part1():
    assertpy.assert_that(passport_processing.calc_passports_with_all_attributes()).is_equal_to(2)


def test_example_input_result_part2():
    assertpy.assert_that(passport_processing_valid.calc_valid_passports()).is_equal_to(4)
    assertpy.assert_that(passport_processing_invalid.calc_valid_passports()).is_equal_to(0)
