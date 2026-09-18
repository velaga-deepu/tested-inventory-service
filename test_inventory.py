"""
Tests for InventoryService.
Run with: pytest
Each function starting with 'test_' is one independent check.
"""

import pytest
from inventory import InventoryService, InsufficientStockError, ItemNotFoundError


def test_add_new_item():
    inv = InventoryService()
    inv.add_item("Notebook", 10)
    assert inv.get_quantity("Notebook") == 10


def test_add_item_increases_existing_quantity():
    inv = InventoryService()
    inv.add_item("Pen", 5)
    inv.add_item("Pen", 3)
    assert inv.get_quantity("Pen") == 8


def test_add_item_rejects_zero_or_negative_quantity():
    inv = InventoryService()
    with pytest.raises(ValueError):
        inv.add_item("Pencil", 0)


def test_remove_stock_reduces_quantity():
    inv = InventoryService()
    inv.add_item("Notebook", 10)
    inv.remove_stock("Notebook", 4)
    assert inv.get_quantity("Notebook") == 6


def test_remove_stock_fails_if_not_enough_available():
    inv = InventoryService()
    inv.add_item("Notebook", 3)
    with pytest.raises(InsufficientStockError):
        inv.remove_stock("Notebook", 5)


def test_remove_stock_fails_for_unknown_item():
    inv = InventoryService()
    with pytest.raises(ItemNotFoundError):
        inv.remove_stock("Ghost Item", 1)


def test_get_quantity_fails_for_unknown_item():
    inv = InventoryService()
    with pytest.raises(ItemNotFoundError):
        inv.get_quantity("Unknown")


def test_low_stock_items_returns_correct_items():
    inv = InventoryService()
    inv.add_item("Notebook", 2)
    inv.add_item("Pen", 20)
    inv.add_item("Eraser", 5)

    low_stock = inv.low_stock_items(threshold=5)

    assert "Notebook" in low_stock
    assert "Eraser" in low_stock
    assert "Pen" not in low_stock


def test_total_items_sums_all_quantities():
    inv = InventoryService()
    inv.add_item("Notebook", 10)
    inv.add_item("Pen", 5)
    assert inv.total_items() == 15
