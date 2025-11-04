"""
Docstring:

Inventory system module for managing stock data.
"""

import json
from datetime import datetime


def add_item(stock_data, item="default", qty=0, logs=None):
    """
    Add a specified quantity of an item to the inventory.

    Args:
        item (str): Name of the item to add.
        qty (int or float): Quantity to add to the inventory.
        logs (list, optional): List to record activity logs.

    Returns:
        None
    """
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print("Invalid input types. 'item' must be string and 'qty' must be number.")
        return
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(stock_data, item, qty):
    """
    Remove a specified quantity of an item from the inventory.

    Args:
        item (str): Name of the item to remove.
        qty (int or float): Quantity to remove from the inventory.

    Logs:
        A warning if the item does not exist in inventory.

    Returns:
        None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock data.")


def get_qty(stock_data, item):
    """
    Retrieve the quantity of a given item from the inventory.

    Args:
        item (str): The name of the item to check.

    Returns:
        int or float: Quantity available in stock for the specified item.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file into the stock_data dictionary.

    Args:
        file (str): Path to the JSON file containing saved inventory data.

    Returns:
        dict: The loaded stock data.
    """
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(stock_data, file="inventory.json"):
    """
    Save the current inventory data to a JSON file.

    Args:
        file (str): Path to the JSON file where data will be saved.

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data(stock_data):
    """
    Print a report of all items and their quantities in the inventory.

    Returns:
        None
    """
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


def check_low_items(stock_data, threshold=5):
    """
    Identify items with quantities below a given threshold.

    Args:
        threshold (int or float): Minimum acceptable quantity.

    Returns:
        list: List of item names that are below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """
    Main execution function that demonstrates the inventory system workflow.

    - Initializes logging.
    - Adds and removes items.
    - Checks stock levels.
    - Saves and loads data.
    - Prints a summary report.

    Returns:
        None
    """
    stock_data = {}
    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", -2)
    add_item(stock_data, 123, "ten")
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)
    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)


main()
