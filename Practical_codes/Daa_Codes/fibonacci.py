import time


def fibonacci_recursive(n):
  """Calculates the n-th Fibonacci number using recursion."""
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
  """Calculates the n-th Fibonacci number using iteration (non-recursive)."""
  if n <= 0:
    return 0
  elif n == 1:
    return 1

  a, b = 0, 1
  for _ in range(2, n + 1):
    a, b = b, a + b
  return b


def main():
  print("=== Fibonacci Calculator (Iterative vs. Recursive) ===")
  try:
    # Ask for dynamic input
    user_input = input("Enter a non-negative integer for n: ")
    n = int(user_input)

    if n < 0:
      print("Error: Please enter a number greater than or equal to 0.")
      return

    print(f"\nCalculating for n = {n}...\n")

    start_time = time.perf_counter()
    result_iterative = fibonacci_iterative(n)
    end_time = time.perf_counter()

    print(f"Iterative Result: {result_iterative}")
    print(f"Iterative Time:   {(end_time - start_time):.8f} seconds\n")

    if n > 35:
      print(
          "⚠️ Warning: n > 35 will cause the recursive approach to run very"
          " slowly (O(2^n) complexity)."
      )
      choice = (
          input("Do you still want to run the recursive method? (y/n): ")
          .strip()
          .lower()
      )
      if choice != "y":
        print("Skipping recursive method.")
        return

    start_time = time.perf_counter()
    result_recursive = fibonacci_recursive(n)
    end_time = time.perf_counter()

    print(f"Recursive Result: {result_recursive}")
    print(f"Recursive Time:   {(end_time - start_time):.8f} seconds")

  except ValueError:
    print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
  main()
