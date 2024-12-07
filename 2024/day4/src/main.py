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


def process_data(data: str) -> list[list[str]]:
    """
    Process the raw data and return 2D grid
    :param data: raw data as a string
    :return: 2D grid
    """
    # split rows
    rows = data.splitlines()
    # split each row into a list of characters
    return [list(row) for row in rows]


def count_xmas_occurrences(grid: list[list[str]]) -> int:
    """
    Given a 2D array of characters, count the number of occurrences of the word "XMAS" in the grid.
    occurrences may be horizontal, vertical, or diagonal in any direction.
    :param grid: 2D array of characters
    :return: number of occurrences of "XMAS" in the grid
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    target = "XMAS"
    rev_target = target[::-1]  # "SAMX"

    # Directions to search: (dr, dc)
    # Reduced directions since we are checking for the reversed word:
    # Right, Down, Diagonal Down-Right, Diagonal Down-Left
    directions = [
        (0, 1),  # horizontal right
        (1, 0),  # vertical down
        (1, 1),  # diagonal down-right
        (1, -1)  # diagonal down-left
    ]

    def word_in_range(row, col):
        return 0 <= row < rows and 0 <= col < cols

    count = 0
    for r in range(rows):
        for c in range(cols):
            # Check each direction from (r,c)
            for dr, dc in directions:
                # Check if we can read 4 characters along this direction
                end_r = r + 3 * dr
                end_c = c + 3 * dc

                if word_in_range(end_r, end_c):
                    # Collect the 4-character sequence
                    seq = []
                    for i in range(4):
                        rr = r + i * dr
                        cc = c + i * dc
                        seq.append(grid[rr][cc])
                    seq = "".join(seq)

                    if seq == target or seq == rev_target:
                        count += 1
    return count


def count_x_shapes(grid: list[list[str]]) -> int:
    """
    Given a 2D array of characters, count the number of X shaped MAS occurrences.
    :param grid: 2D array of characters
    :return: number of occurrences of X-MAS in the grid
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    target = "MAS"
    rev_target = target[::-1]  # "SAM"

    count = 0
    # Given an array of NxM iterate over N-1xM-1 to find the center of the X, which is an A
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check if current cell can be the center 'A'
            if grid[r][c] == 'A':
                # Word from top left to bottom right
                diagonal_left = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
                # Word from top right to bottom left
                diagonal_right = grid[r + 1][c - 1] + grid[r][c] + grid[r - 1][c + 1]
                # Check for target
                if (diagonal_left == target or diagonal_left == rev_target) and (
                        diagonal_right == target or diagonal_right == rev_target):
                    count += 1
    return count


def run_solution_p1(data: str) -> int:
    """
    Run the solution of the first part with the given data
    :param data: raw data as a string
    :return: solution to the puzzle
    """
    # Process the data
    grid = process_data(data)

    # count xmas occurrences in the grid
    result = count_xmas_occurrences(grid)
    return result


def run_solution_p2(data: str) -> int:
    """
        Run the solution of the second part with the given data
        :param data: raw data as a string
        :return: solution to the puzzle
        """
    grid = process_data(data)

    # count x-mas occurrences in the grid
    result = count_x_shapes(grid)
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
