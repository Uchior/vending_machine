from dataclasses import dataclass
from vending_machine.domain.models.drink import Drink


@dataclass
class Slot:
    slot_number: str
    drink: Drink
    stock: int

    def is_available(self) -> bool:
        return self.stock > 0

    def dispense(self) -> Drink:
        if self.stock <= 0:
            raise ValueError("Out of stock")
        self.stock -= 1
        return self.drink

    def refill(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.stock += quantity

    def replace_drink(self, new_drink: Drink, new_stock: int) -> None:
        if new_stock < 1:
            raise ValueError("New stock must be at least 1")
        self.drink = new_drink
        self.stock = new_stock
