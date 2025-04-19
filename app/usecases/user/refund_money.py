from domain.models.vending_machine import VendingMachine


class RefundMoneyCase:
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    def execute(self) -> str:
        refund = self.vending_machine.refund()
        return f"お釣りは{refund.amount}円です。"
