from domain.models.vending_machine import VendingMachine
from domain.models.money import Money


class PurchaseDrinkCase:
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    def execute(self, slot_number: str, inserted_money: int) -> (Money, str):
        """Purchase a drink from the vending machine."""
        money = Money(inserted_money)
        change, drink_name = self.vending_machine.purchase(slot_number, money)
        return f"'{drink_name}'を購入しました。お釣りは{change.amount}円です。"
