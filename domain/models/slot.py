from dataclasses import dataclass
from domain.models.drink import Drink

@dataclass
class Slot:
    slot_number: str
    drink: Drink
    stock: int

    def is_available(self) -> bool:
        """Check if the slot is available."""
        return self.stock > 0

    def dispense(self) -> Drink:
        if self.stock <= 0:
            raise ValueError("Out of stock")
        self.stock -= 1
        return self.drink
