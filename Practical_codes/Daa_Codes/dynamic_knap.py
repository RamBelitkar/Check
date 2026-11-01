def knapsack_01(capacity, weights, values, n):
  """Solves the 0-1 Knapsack problem using Dynamic Programming."""
  dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

  for i in range(1, n + 1):
    for w in range(1, capacity + 1):
      if weights[i - 1] <= w:
        include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]

        exclude_item = dp[i - 1][w]
 
        dp[i][w] = max(include_item, exclude_item)
      else:
        dp[i][w] = dp[i - 1][w]

  max_value = dp[n][capacity]
  w = capacity
  selected_items = []
  for i in range(n, 0, -1):
    if max_value <= 0:
      break
    if max_value == dp[i - 1][w]:
      continue
    else:
      selected_items.append(i)
      max_value -= values[i - 1]
      w -= weights[i - 1]

  return dp[n][capacity], selected_items


def main():
  print("=== 0-1 Knapsack Problem (Dynamic Programming) ===")
  print("What to provide as input:")
  print("1. Maximum capacity of the knapsack (integer).")
  print("2. Total number of items (integer).")
  print("3. Weight and Value for each item (integers).\n" + "-" * 50)

  try:
    capacity = int(
        input("Enter the maximum capacity of the knapsack: ").strip()
    )
    if capacity <= 0:
      print("Capacity must be greater than 0.")
      return

    n = int(input("Enter the total number of items: ").strip())
    if n <= 0:
      print("Number of items must be at least 1.")
      return

    weights = []
    values = []

    print("\nEnter weight and value for each item:")
    for i in range(1, n + 1):
      print(f"\n--- Item {i} ---")
      w = int(input(f"Enter weight for item {i}: ").strip())
      v = int(input(f"Enter value for item {i}: ").strip())

      if w <= 0 or v < 0:
        print("Error: Weight must be > 0 and value must be >= 0.")
        return

      weights.append(w)
      values.append(v)

    max_val, selected = knapsack_01(capacity, weights, values, n)

    print("\n" + "=" * 40)
    print("OPTIMAL SOLUTION RESULTS")
    print("=" * 40)
    print(f"Maximum Value in Knapsack: {max_val}\n")
    print(f"Selected Items (Item Numbers): {selected}")
    print(f"{'Item':<8} | {'Weight':<8} | {'Value':<8}")
    print("-" * 30)

    for idx in selected:
      print(f"Item {idx:<3} | {weights[idx-1]:<8} | {values[idx-1]:<8}")

  except ValueError:
    print("Invalid input! Please enter valid integer values.")


if __name__ == "__main__":
  main()
