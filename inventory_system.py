"""Inventory management system for tracking stock items."""

import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item: Name of the item to add
        qty: Quantity to add
        logs: List to store log entries
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove an item from the inventory.

    Args:
        item: Name of the item to remove
        qty: Quantity to remove
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory")


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item: Name of the item to check

    Returns:
        Quantity of the item
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file: Path to the JSON file
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(
            f"File '{file}' not found. Starting with empty inventory."
        )
    except json.JSONDecodeError:
        print(
            f"Error decoding JSON from '{file}'. "
            f"Starting with empty inventory."
        )


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file: Path to the JSON file
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print the current inventory report."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(item, "->", quantity)


def check_low_items(threshold=5):
    """
    Check for items below a certain threshold.

    Args:
        threshold: Minimum quantity threshold

    Returns:
        List of items below the threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    # Type validation could be added here for production use
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Removed eval() - use safe alternatives for dynamic execution


main()
