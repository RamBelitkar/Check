class Item:
  """Represents an item with a weight, value, and its value-to-weight ratio."""

  def __init__(self, index, weight, value):
    self.index = index
    self.weight = weight
    self.value = value
    self.ratio = value / weight


def fractional_knapsack(capacity, items):
  """Solves the fractional knapsack problem using a greedy strategy.

  Greedy Choice: Sort items by value-to-weight ratio in descending order and
  pick the most valuable units first.
  """
  items.sort(key=lambda x: x.ratio, reverse=True)

  total_value = 0.0
  current_weight = 0.0
  selection_details = []

  for item in items:
    if capacity <= 0:
      break

    if item.weight <= capacity:
  
      capacity -= item.weight
      current_weight += item.weight
      total_value += item.value
      selection_details.append(
          (item.index, item.weight, item.value, 1.0)
      )  
    else:
      fraction = capacity / item.weight
      current_weight += item.weight * fraction
      total_value += item.value * fraction
      selection_details.append(
          (item.index, item.weight, item.value, fraction)
      )
      capacity = 0  

  return total_value, selection_details


def main():
  print("=== Fractional Knapsack Problem (Greedy Strategy) ===")

  try:
    capacity = float(
        input("Enter the maximum capacity of the knapsack: ").strip()
    )
    if capacity <= 0:
      print("Capacity must be greater than 0.")
      return

    n = int(input("Enter the total number of items: ").strip())
    if n <= 0:
      print("Number of items must be at least 1.")
      return

    items = []
    print("\nEnter the weight and value for each item:")
    for i in range(1, n + 1):
      print(f"\n--- Item {i} ---")
      weight = float(input(f"Enter weight for item {i}: ").strip())
      value = float(input(f"Enter value for item {i}: ").strip())

      if weight <= 0 or value < 0:
        print("Error: Weight must be > 0 and value must be >= 0.")
        return

      items.append(Item(i, weight, value))

    max_value, details = fractional_knapsack(capacity, items)

    print("\n" + "=" * 40)
    print("OPTIMAL SOLUTION RESULTS")
    print("=" * 40)
    print(f"Maximum Value in Knapsack: {max_value:.2f}\n")
    print("Breakdown of items included:")
    print(f"{'Item':<8} | {'Weight':<8} | {'Value':<8} | {'Fraction Taken'}")
    print("-" * 45)

    for index, weight, value, fraction in details:
      fraction_percentage = fraction * 100
      print(
          f"Item {index:<3} | {weight:<8.1f} | {value:<8.1f} |"
          f" {fraction_percentage:.1f}%"
      )

  except ValueError:
    print("Invalid input! Please enter valid numeric values.")


if __name__ == "__main__":
  main()
