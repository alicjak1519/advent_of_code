from assertpy import assertpy

from .password_philosophy import PasswordPhilosophy


def test_example_input_result():
    example_philosophy = PasswordPhilosophy("inputs/day2_example_input.csv")
    assertpy.assert_that(example_philosophy.count_valid_passwords()).is_equal_to(2)
