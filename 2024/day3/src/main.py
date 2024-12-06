import re


def load_data(file_path: str) -> str:
    """
    Loads the data from the file
    :param file_path: path to the file
    :return: raw data as a string
    """
    with open(file_path, "r") as file:
        # read the data from the file and return a raw string
        return file.read()


def process_data(data: str) -> list[tuple[int, int]]:
    """
    Process the raw data and return list of (X, Y) for the function mul(X, Y)
    :param data: raw data as a string
    :return: list of (X, Y)
    """
    # Define the pattern to match mul(X,Y) where X and Y are integers with 1 to 3 digits
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # Find all matches and convert them to integer pairs
    matches = re.findall(pattern, data)
    return [(int(x), int(y)) for x, y in matches]

def process_data_v2(data: str) -> list[tuple[int, int]]:
    """
    Process the raw data and return list of (X, Y) for the function mul(X, Y); having into account the do and don't instructions
    :param data: raw data as a string
    :return: list of (X, Y)
    """
    # Split the input string into sections using "do()" and "don't()"
    sections = re.split(r"do\(\)|don't\(\)", data)

    # Find all occurrences of "do()" and "don't()" to track enabling/disabling
    controls = re.findall(r"do\(\)|don't\(\)", data)

    # Start with mul(X,Y) enabled
    enabled = True
    result = []

    # Iterate over sections and their corresponding controls
    for i, section in enumerate(sections):
        if enabled:
            # Extract valid mul(X,Y) with numbers up to 3 digits in the active section
            pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
            matches = re.findall(pattern, section)
            result.extend([(int(x), int(y)) for x, y in matches])

        # Update enabled status based on the current control
        if i < len(controls):
            enabled = controls[i] == "do()"

    return result


def run_solution_p1(data: str) -> int:
    """
    Run the solution of the first part with the given data
    :param data: raw data as a string
    :return: solution to the puzzle
    """
    # Process the data
    mul_inputs = process_data(data)

    # multiply pairs and sum the results
    result = sum([x * y for x, y in mul_inputs])
    return result


def run_solution_p2(data: str) -> int:
    """
        Run the solution of the second part with the given data
        :param data: raw data as a string
        :return: solution to the puzzle
        """
    # Process the data
    mul_inputs = process_data_v2(data)

    # multiply pairs and sum the results
    result = sum([x * y for x, y in mul_inputs])
    return result


if __name__ == "__main__":
    # Load the data from the file
    raw_input = load_data("data/real_input.txt")

    # Run the solution with the data
    p1_sol = run_solution_p1(raw_input)
    p2_sol = run_solution_p2(raw_input)

    # Print the result
    print(f"Part 1 Solution: {p1_sol}")
    print(f"Part 2 Solution: {p2_sol}")
