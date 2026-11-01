def solve_n_queens_fixed_first(n, first_col):
  """Solves the n-Queens problem using backtracking,

  given that the first queen is already fixed at row 0, column first_col.
  """
  board = [[0] * n for _ in range(n)]

  board[0][first_col] = 1

  cols = {first_col}
  diag1 = {0 - first_col}  # r - c
  diag2 = {0 + first_col}  # r + c

  def backtrack(row):
    if row == n:
      return True

    if row == 0:
      return backtrack(row + 1)

    for col in range(n):
      if col in cols or (row - col) in diag1 or (row + col) in diag2:
        continue

      board[row][col] = 1
      cols.add(col)
      diag1.add(row - col)
      diag2.add(row + col)

      if backtrack(row + 1):
        return True

      board[row][col] = 0
      cols.remove(col)
      diag1.remove(row - col)
      diag2.remove(row + col)

    return False

  success = backtrack(0)
  return board if success else None


def print_board(board):
  """Utility function to print the chessboard matrix."""
  if not board:
    print(
        " No valid configuration found with the first queen at that"
        " position."
    )
    return

  n = len(board)
  print(f"\nFinal {n}x{n} Queens Matrix:")
  print("-" * (n * 4 + 1))
  for row in board:
    print("| " + " | ".join("Q" if cell == 1 else "." for cell in row) + " |")
    print("-" * (n * 4 + 1))


def main():
  print("=== n-Queens Problem with Pre-placed First Queen ===")
  try:
    n = int(input("Enter the board size n (e.g., 4, 8): ").strip())
    if n < 4:
      print(
          "Note: For n = 1, 2, or 3, valid solutions are limited or non-existent"
          " (except n=1)."
      )

    first_col = int(
        input(f"Enter the column for the first queen (0 to {n-1}): ").strip()
    )

    if not (0 <= first_col < n):
      print(
          f"Error: Column index must be between 0 and {n-1} for an {n}x{n}"
          " board."
      )
      return

    print(f"\nPlacing first queen at Row 0, Column {first_col}...")

    result_board = solve_n_queens_fixed_first(n, first_col)

    print_board(result_board)

  except ValueError:
    print("Invalid input! Please enter valid integers.")


if __name__ == "__main__":
  main()
