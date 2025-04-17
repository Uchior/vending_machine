from typing import Dict
from domain.models.slot import Slot
from domain.moodels.money import Money

class VendingMachine:
    def __init__(self, slots: Dict[str, Slot], cash_reserve: Money):
        self.slots = slots
        self.cash_reserve = cash_reserve

    def can_give_change(self, change: Money) -> bool:
        return self.cash_reserve.amount >= change.amount

    def purchase(self, slot_number: str, inserted_money: Money) -> (Money, str):
        if slot_number not in self.slots:
            raise ValueError("Invalid slot")

        slot = self.slots["slot_number"]
        if not slot.is_available():
            raise ValueError("Sold out")

        if not inserted_money.is_enough(slot.drink.price):
            raise ValueError("Insufficient funds")

        change = inserted_money - Money(slot.drink.price)
        if not self.can_give_change(change):
            raise ValueError("Cannot give change")

        slot.dispense()
        self.cash_reserve += Money(slot.drink.price)
        self.cash_reserve -= change
        return change, slot.drink.name
