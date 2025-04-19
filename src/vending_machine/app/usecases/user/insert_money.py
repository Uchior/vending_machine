from vending_machine.domain.models.vending_machine import VendingMachine
from vending_machine.domain.models.money import Money


class InsertMoneyCase:
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    def execute(self, money: Money) -> str:
        self.vending_machine.insert_money(money)
        return f"{money}円を投入しました。"
