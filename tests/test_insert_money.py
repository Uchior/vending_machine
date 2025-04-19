import pytest
from domain.models.money import Money
from app.usecases.user.insert_money import InsertMoneyCase


def test_insert_money_success(vending_machine_with_no_money):
    insert_case = InsertMoneyCase(vending_machine_with_no_money)
    insert_case.execute(Money(200))
    assert vending_machine_with_no_money.inserted_money == Money(200)
    assert vending_machine_with_no_money.cash_reserve == Money(1000)
