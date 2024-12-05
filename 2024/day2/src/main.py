from typing import Tuple, Union


def load_data(file_path: str) -> str:
    """
    Loads the data from the file
    :param file_path: path to the file
    :return: raw data as a string
    """
    with open(file_path, "r") as file:
        # read the data from the file and return a raw string
        return file.read()


def process_data(data: str) -> list[list[int]]:
    """
    Process the raw data and return list of reports
    :param data: raw data as a string
    :return: list of reports
    """
    # Split the string into lines
    lines = data.splitlines()

    return [list(map(int, line.split())) for line in lines]


def is_report_safe(report: list[int]) -> bool:
    """
    Check if the report is safe; a report is safe if all levels are increasing or decreasing, as well as if the difference between two levels is more than 1 and less than 3.
    :param report: the report
    :return: True if the report is safe, False otherwise
    """
    return ((all(report[i] < report[i + 1] for i in range(len(report) - 1)) or # all increasing
            all(report[i] > report[i + 1] for i in range(len(report) - 1))) # all decreasing
            and all(abs(report[i] - report[i + 1]) in (1, 2, 3) for i in range(len(report) - 1))) # difference is [1, 3]

def is_report_safe_v2(report: list[int]) -> bool:
    """
    Check if the report is safe; a report is safe if all levels are increasing or decreasing, as well as if the difference between two levels is more than 1 and less than 3.
    This version also takes account of the error dampener, which tries to remove one level from the report to make it safe.
    :param report: the report
    :return: True if the report is safe, False otherwise
    """
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_report_safe(modified_report):
            return True

    return False

def run_solution_p1(data: str) -> int:
    """
    Run the solution of the first part with the given data
    :param data: raw data as a string
    :return: solution to the puzzle
    """
    # Process the data
    reports = process_data(data)

    # calculate the number of safe reports
    safe_reports = len([report for report in reports if is_report_safe(report)])

    return safe_reports


def run_solution_p2(data: str) -> int:
    """
        Run the solution of the second part with the given data
        :param data: raw data as a string
        :return: solution to the puzzle
        """
    # Process the data
    reports = process_data(data)

    # calculate the number of safe reports
    safe_reports = len([report for report in reports if is_report_safe_v2(report)])

    return safe_reports

if __name__ == "__main__":
    # Load the data from the file
    raw_input = load_data("data/real_input.txt")

    # Run the solution with the data
    p1_sol = run_solution_p1(raw_input)
    p2_sol = run_solution_p2(raw_input)

    # Print the result
    print(f"Part 1 Solution: {p1_sol}")
    print(f"Part 2 Solution: {p2_sol}")
