from points_decorator import points

import inspect

class TestProblem1:
    @points(2, "Problem 1, Part 1: Function 'fahr_to_celsius' is not correctly defined!")
    def test_problem_1_part_1_fuction(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        assert inspect.isfunction(variables['fahr_to_celsius'])

        assert round(variables['fahr_to_celsius'](48),2) == 8.89
        assert round(variables['fahr_to_celsius'](71),2) == 21.67
        

    @points(1, "Problem 1, Part 1: Function 'fahr_to_celsius' does not have a docstring!")
    def test_problem_1_part_1_docstring(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        assert variables['fahr_to_celsius'].__doc__
