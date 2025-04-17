from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: int  # 日本円

    def __add__(self, other: 'Money') -> 'Money':
        return Money(self.amount + other.amount)

    def __sub__(self, other: 'Money') -> 'Money':
        if self.amount < other.amount:
            raise ValueError("Not enough money to subtract")
        return Money(self.amount - other.amount)

    def is_enough(self, price: int) -> bool:
        """Check if the amount is enough to cover the price."""
        return self.amount >= price
