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
