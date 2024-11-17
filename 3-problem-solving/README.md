# Average Price Calculator

## Overview

This Python project calculates the average price of items within a specific category from a given dataset. It includes robust error handling, input validation, and detailed output to explain the calculations.

## Features
- Calculates the average price for items in a specified category.
- Validates input data to ensure it follows the expected structure.
- Supports only specific categories: **electronics**, **clothing**, and **home_appliances**.
- Provides detailed breakdown and explanation of the calculation process.
- Handles invalid inputs gracefully with descriptive error messages.

## Requirements
- Python 3.6 or higher.

## Installation
1. Ensure you have Python 3.6+ installed:
   ```bash
   python --version
   ```
2. Run the script directly:
   ```bash
   python main.py
   ```

## Usage
### Example Input
```python
data = [
    {"id": 1, "category": "electronics", "price": 199.99},
    {"id": 2, "category": "clothing", "price": 49.99},
    {"id": 3, "category": "electronics", "price": 299.99},
    {"id": 4, "category": "electronics", "price": 99.99},
    {"id": 5, "category": "clothing", "price": 19.99},
    {"id": 6, "category": "electronics", "price": 149.99},
    {"id": 7, "category": "home_appliances", "price": 89.99},
    {"id": 8, "category": "electronics", "price": 249.99},
]
target_category = "electronics"
```

### Example Output
```plaintext
The average price for the category 'electronics' is: $199.99

**Details**:
The following items were considered for the calculation:
  - ID: 1, Price: $199.99
  - ID: 3, Price: $299.99
  - ID: 4, Price: $99.99
  - ID: 6, Price: $149.99
  - ID: 8, Price: $249.99

**Explanation**:
The total price of the 5 items in the category is: $999.95
The average price is calculated as: 999.95 / 5 = $199.99
```

### How to Use
1. Modify the `data` list to include your dataset.
2. Change the `target_category` variable to the desired category (`electronics`, `clothing`, or `home_appliances`).
3. Run the script, and the output will display the average price along with a detailed breakdown.

## Input Validation
The script performs the following checks:
- **Data Type**: Ensures `data` is a list and each item is a dictionary.
- **Required Keys**: Each dictionary must include `category` and `price` keys.
- **Allowed Categories**: Only `electronics`, `clothing`, and `home_appliances` are supported.
- **Price Validation**: Ensures prices are positive numbers (integer or float).

## Error Handling
The script raises detailed errors for invalid inputs:
- If `data` is not a list or contains invalid items, a `ValueError` or `KeyError` is raised.
- If the category is not one of the allowed values, a `ValueError` is raised.

### Example Error Messages
1. Missing keys:
   ```plaintext
   Error: Each item must contain 'category' and 'price' keys.
   ```
2. Invalid category:
   ```plaintext
   Error: The 'category' must be one of {'electronics', 'clothing', 'home_appliances'}.
   ```
3. Negative price:
   ```plaintext
   Error: The 'price' value cannot be negative.
   ```

## Code Structure
- `validate_data`: Validates the dataset and target category.
- `calculate_average_price`: Filters data, calculates the average price, and returns detailed results.
- Main script: Processes the input, calls the functions, and displays output.

## Extensibility
- **Additional Categories**: To add more categories, update the `ALLOWED_CATEGORIES` set in the `validate_data` function.
- **Advanced Analysis**: Add more statistical calculations (e.g., median, mode) by extending the `calculate_average_price` function.