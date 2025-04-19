from vending_machine.domain.models.vending_machine import VendingMachine


class PurchaseDrinkCase:
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    def execute(self, slot_number: str) -> str:
        drink_name = self.vending_machine.purchase(slot_number)
        return f"'{drink_name}'を購入しました。"
