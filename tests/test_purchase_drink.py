import pytest
from domain.models.money import Money
from app.usecases.user.purchase_drink import PurchaseDrinkCase
from app.usecases.user.insert_money import InsertMoneyCase


def test_purchase_drink_success(vending_machine_with_inserted_money):
    purchase_case = PurchaseDrinkCase(vending_machine_with_inserted_money)
    result = purchase_case.execute("A1")
    assert result == "'Coke'を購入しました。"


def test_purchase_drink_insufficient_funds(vending_machine_with_no_money):
    purchase_case = PurchaseDrinkCase(vending_machine_with_no_money)
    with pytest.raises(ValueError, match="Insufficient funds"):
        assert purchase_case.execute("A1")


def test_purchase_drink_sold_out(vending_machine_with_inserted_money):
    purchase_case = PurchaseDrinkCase(vending_machine_with_inserted_money)
    with pytest.raises(ValueError, match="Sold out"):
        assert purchase_case.execute("B1")
