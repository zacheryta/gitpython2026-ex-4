#!/usr/bin/env python3
from points_decorator import points
import pathlib
import inspect
class TestProblem2:
    @points(2, "Problem 2, Part 1: Function 'temp_classifier' is not correctly defined!")
    def test_problem_2_part_1_fuction(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        assert inspect.isfunction(variables['temp_classifier'])

        assert variables['temp_classifier'](16.5) == 3
        assert variables['temp_classifier'](2) == 2
        assert variables['temp_classifier'](-5) == 0

    @points(1, "Problem 2, Part 2: Function 'temp_classifier' does not have a docstring!")
    def test_problem_2_part_1_docstring(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        assert variables['temp_classifier'].__doc__
   