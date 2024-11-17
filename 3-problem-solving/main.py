def validate_data(data, target_category):
    """
    Validates the input data and category for the calculate_average_price function.

    Parameters:
    data (list): List of dictionaries containing item data.
    target_category (str): Category to filter items by.

    Raises:
    ValueError: If the data or category is invalid.
    KeyError: If required keys are missing in the data items.
    """
    # Allowed categories
    ALLOWED_CATEGORIES = {"electronics", "clothing", "home_appliances"}

    # Error messages
    ERROR_INVALID_DATA_TYPE = "The data parameter must be a list of dictionaries."
    ERROR_INVALID_CATEGORY_TYPE = "The target_category parameter must be a string."
    ERROR_INVALID_ITEM_TYPE = "Each item in the data list must be a dictionary."
    ERROR_MISSING_KEYS = "Each item must contain 'category' and 'price' keys."
    ERROR_INVALID_ID_VALUE = "The 'id' value must be a number (int)."
    ERROR_INVALID_CATEGORY_VALUE = "The 'category' value must be a string."
    ERROR_INVALID_CATEGORY_NAME = f"The 'category' must be one of {ALLOWED_CATEGORIES}."
    ERROR_INVALID_PRICE_VALUE = "The 'price' value must be a number (int or float)."
    ERROR_NEGATIVE_PRICE = "The 'price' value cannot be negative."

    # Validate inputs
    if not isinstance(data, list):
        raise ValueError(ERROR_INVALID_DATA_TYPE)
    if not isinstance(target_category, str):
        raise ValueError(ERROR_INVALID_CATEGORY_TYPE)
    if target_category not in ALLOWED_CATEGORIES:
        raise ValueError(ERROR_INVALID_CATEGORY_NAME)

    # Validate each item in the list
    for item in data:
        if not isinstance(item, dict):
            raise ValueError(ERROR_INVALID_ITEM_TYPE)
        if "category" not in item or "price" not in item:
            raise KeyError(ERROR_MISSING_KEYS)
        if not isinstance(item["id"], (int, float)):
            raise ValueError(ERROR_INVALID_ID_VALUE)
        if not isinstance(item["category"], str):
            raise ValueError(ERROR_INVALID_CATEGORY_VALUE)
        if item["category"] not in ALLOWED_CATEGORIES:
            raise ValueError(ERROR_INVALID_CATEGORY_NAME)
        if not isinstance(item["price"], (int, float)):
            raise ValueError(ERROR_INVALID_PRICE_VALUE)
        if item["price"] < 0:
            raise ValueError(ERROR_NEGATIVE_PRICE)


def calculate_average_price(data, target_category):
    """
    Calculates the average price for items in the specified category.

    Parameters:
    data (list): List of dictionaries containing item data.
    target_category (str): Category to filter items by.

    Returns:
    tuple: A tuple containing the average price (float) and the list of relevant items.
    """
    # Validate data and category
    validate_data(data, target_category)

    # Filter items by the target category
    filtered_items = [item for item in data if item['category'] == target_category]

    # Calculate the average price
    if filtered_items:
        total_price = sum(item['price'] for item in filtered_items)
        average_price = total_price / len(filtered_items)
        return round(average_price, 2), filtered_items
    else:
        return None, []  # Return None if no items match the category


# Example data
data = [
    {"id": 1, "category": "electronics", "price": 199.99},
    {"id": 2, "category": "clothing", "price": 49.99},
    {"id": 3, "category": "electronics", "price": 299.99},
    {"id": 4, "category": "electronics", "price": 99.99},
    {"id": 5, "category": "clothing", "price": 19.99},
    {"id": 6, "category": "electronics", "price": 149.99},
    {"id": 7, "category": "home_appliances", "price": 89.99},
    {"id": 8, "category": "electronics", "price": 249.99}
]

try:
    target_category = "electronics"
    average_price, relevant_items = calculate_average_price(data, target_category)

    if average_price is not None:
        print(f"The average price for the category '{target_category}' is: ${average_price}")
        print("\n**Details**:")
        print(f"The following items were considered for the calculation:")
        for item in relevant_items:
            print(f"  - ID: {item['id']}, Price: ${item['price']}")
        print("\n**Explanation**:")
        total_price = sum(item['price'] for item in relevant_items)
        print(f"The total price of the {len(relevant_items)} items in the category is: ${total_price}")
        print(f"The average price is calculated as: {total_price} / {len(relevant_items)} = ${average_price}")
    else:
        print(f"No items found in the category '{target_category}'.")
except (ValueError, KeyError) as e:
    print(f"Error: {e}")
