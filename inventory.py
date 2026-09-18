"""
Inventory Service
Core logic for managing stock items: add, remove, update quantity, and check stock levels.
Kept separate from any interface (console/web) so it can be tested independently.
"""


class InsufficientStockError(Exception):
    """Raised when trying to remove more stock than is available."""
    pass


class ItemNotFoundError(Exception):
    """Raised when referencing an item that doesn't exist in the inventory."""
    pass


class InventoryService:
    def __init__(self):
        self.items = {}  # item_name -> quantity

    def add_item(self, name, quantity):
        """Add a new item, or increase quantity if it already exists."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items[name] = self.items.get(name, 0) + quantity

    def remove_stock(self, name, quantity):
        """Reduce stock for an item. Raises an error if not enough stock exists."""
        if name not in self.items:
            raise ItemNotFoundError(f"'{name}' not found in inventory")
        if self.items[name] < quantity:
            raise InsufficientStockError(
                f"Cannot remove {quantity} of '{name}', only {self.items[name]} in stock"
            )
        self.items[name] -= quantity

    def get_quantity(self, name):
        """Return current stock level for an item."""
        if name not in self.items:
            raise ItemNotFoundError(f"'{name}' not found in inventory")
        return self.items[name]

    def low_stock_items(self, threshold=5):
        """Return a list of item names at or below the given threshold."""
        return [name for name, qty in self.items.items() if qty <= threshold]

    def total_items(self):
        """Return the total quantity of all items combined."""
        return sum(self.items.values())
