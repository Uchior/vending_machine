import pytest
from domain.models.money import Money
from app.usecases.user.refund_money import RefundMoneyCase


def test_refund_money_success(vending_machine_with_inserted_money):
    refund_case = RefundMoneyCase(vending_machine_with_inserted_money)
    refund_amount = refund_case.execute()
    assert refund_amount == "お釣りは200円です。"
    assert vending_machine_with_inserted_money.inserted_money == Money(0)

