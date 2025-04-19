from typing import Dict
from vending_machine.domain.models.slot import Slot
from vending_machine.domain.models.money import Money


class VendingMachine:
    def __init__(self, slots: Dict[str, Slot], cash_reserve: Money):
        self.slots = slots
        self.cash_reserve = cash_reserve
        self.inserted_money = Money(0)

    def insert_money(self, money: Money):
        self.inserted_money += money

    def refund(self) -> Money:
        refund = self.inserted_money
        self.inserted_money = Money(0)
        return refund

    def can_give_change(self, change: Money) -> bool:
        return self.cash_reserve.amount >= change.amount

    def purchase(self, slot_number: str) -> str:
        if slot_number not in self.slots:
            raise ValueError("Invalid slot")

        slot = self.slots[slot_number]
        if not slot.is_available():
            raise ValueError("Sold out")

        if not self.inserted_money.is_enough(slot.drink.price):
            raise ValueError("Insufficient funds")

        change = self.inserted_money - Money(slot.drink.price)
        if not self.can_give_change(change):
            raise ValueError("Cannot give change")

        self.inserted_money -= change
        slot.dispense()
        self.cash_reserve += Money(slot.drink.price)
        return slot.drink.name
