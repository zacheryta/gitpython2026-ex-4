#!/usr/bin/env python3
from points_decorator import points
import os
import sys

# Add the directory containing temp_functions.py to the Python path
script_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(script_dir)


class TestProblem3:
    @points(1, "Problem 3, Part 1: temp_functions.py script file is not found!")
    def test_temp_functions_script_exists(self):
        # Define the path to the script file
        script_path = os.path.join(os.path.dirname(__file__), '..', 'temp_functions.py')

        # Check if the script file exists
        assert os.path.isfile(script_path), f"temp_functions.py script file is not found at {script_path}!"



    @points(1, "Problem 3, Part 2: Loop not found in source code!")
    def test_problem_4_part_1_loop(self, problem3):
        section_data, namespace = problem3
        section = "Part 2"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        source = section_data[section]['source']

        assert any(loop in source for loop in ["for", "while"]), "Loop not found in source code!"


    
    @points(2, "Problem 3, Part 2: Variables 'zeros, ones, twos or threes' are not correctly defined!")
    def test_problem_4_part_1_values(self, problem3):
        section_data, namespace = problem3
        section = "Part 2"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']
        
        assert variables['zeros'] == 137
        assert variables['ones'] == 85
        assert variables['twos'] == 114
        assert variables['threes'] == 0
        
