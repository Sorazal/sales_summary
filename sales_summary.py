# sales_summary.py

def average(numbers):
    """Calculates the average of a list of numbers"""
    return sum(numbers) / len(numbers)

# List of sales
sales = [100, 200, 50, 400, 150]

# Calculations
total_sales = sum(sales)
average_sales = average(sales)
max_sale = max(sales)
min_sale = min(sales)

# Print results
print("=== Sales Summary ===")
print("Total sales:", total_sales)
print("Average sale:", average_sales)
print("Highest sale:", max_sale)
print("Lowest sale:", min_sale)
