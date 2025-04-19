from domain.models.vending_machine import VendingMachine
from domain.models.slot import Slot


class RefillSlotCase:
    def __init__(self, vending_machine: VendingMachine) -> None:
        self.vending_machine = vending_machine

    def execute(self, slot_number: str, quantity: int) -> str:
        if slot_number not in self.vending_machine.slots:
            raise ValueError("Invalid slot")
        slot: Slot = self.vending_machine.slots[slot_number]
        slot.refill(quantity)
        return f"{slot_number}に{quantity}個補充しました。"
