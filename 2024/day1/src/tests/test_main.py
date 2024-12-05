import json
from main import run_solution_p1, run_solution_p2

test_cases_part_1 = ["part_1_test_case_1.json"]
test_cases_part_2 = ["part_2_test_case_1.json"]


def test_run_test_cases_part_1():
    for test_case_json in test_cases_part_1:
        with open(f"data/{test_case_json}", "r") as file:
            # Given
            test_case = json.load(file)
            expected = test_case["expected_result"]
            input_data = test_case["raw_input"]
            # When
            actual = run_solution_p1(input_data)
            # Then
            assert actual == expected, f"Error while testing: {test_case['name']}"


def test_run_test_cases_part_2():
    for test_case_json in test_cases_part_2:
        with open(f"data/{test_case_json}", "r") as file:
            # Given
            test_case = json.load(file)
            expected = test_case["expected_result"]
            input_data = test_case["raw_input"]
            # When
            actual = run_solution_p2(input_data)
            # Then
            assert actual == expected, f"Error while testing: {test_case['name']}"
