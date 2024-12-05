from typing import Tuple


def load_data(file_path: str) -> str:
    """
    Loads the data from the file
    :param file_path: path to the file
    :return: raw data as a string
    """
    with open(file_path, "r") as file:
        # read the data from the file and return a raw string
        return file.read()


def process_data(data: str) -> Tuple[list[int], list[int]]:
    """
    Process the raw data and return both lists of locationIds
    :param data: raw data as a string
    :return: left and right lists of locationIds
    """
    # Split the string into lines
    lines = data.splitlines()

    # Initialize two empty lists
    list1 = []
    list2 = []

    # Process each line
    for line in lines:
        # Split each line into two numbers
        col1, col2 = map(int, line.split())
        list1.append(col1)
        list2.append(col2)

    return list1, list2


def run_solution_p1(data: str) -> int:
    """
    Run the solution of the first part with the given data
    :param data: raw data as a string
    :return: solution to the puzzle
    """
    # Process the data
    list1, list2 = process_data(data)

    # Sort lists
    list1.sort()
    list2.sort()

    # Calculate total distance between each pair of elements
    total_distance = sum(abs(x - y) for x, y in zip(list1, list2))

    return total_distance


def run_solution_p2(data: str) -> int:
    """
    Run the solution of the second part with the given data
    :param data: raw data as a string
    :return: solution to the puzzle
    """
    # Process the data
    list1, list2 = process_data(data)

    # Count occurrences of item from list 1 in list 2
    similarity_score = sum([calculate_similarity_score(item, list2.count(item)) for item in list1])

    return similarity_score

def calculate_similarity_score(item: int, occurrences: int) -> int:
    """
    Calculate the similarity score for an item based on its occurrences
    :param item: the item
    :param occurrences: the number of occurrences
    :return: the similarity score (item times occurrences)
    """
    return item * occurrences


if __name__ == "__main__":
    # Load the data from the file
    raw_input = load_data("data/real_input.txt")

    # Run the solution with the data
    p1_sol = run_solution_p1(raw_input)
    p2_sol = run_solution_p2(raw_input)

    # Print the result
    print(f"Part 1 Solution: {p1_sol}")
    print(f"Part 2 Solution: {p2_sol}")
