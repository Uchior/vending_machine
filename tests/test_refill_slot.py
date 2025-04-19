import pytest
from domain.models.money import Money
from app.usecases.operator.refill_slot import RefillSlotCase


def test_refill_slot_success(vending_machine_with_no_money):
    refill_case = RefillSlotCase(vending_machine_with_no_money)
    result = refill_case.execute("A1", 10)
    assert result == "A1に10個補充しました。"
    assert vending_machine_with_no_money.slots["A1"].stock == 15


def test_refill_slot_invalid_slot(vending_machine_with_no_money):
    refill_case = RefillSlotCase(vending_machine_with_no_money)
    with pytest.raises(ValueError, match="Invalid slot"):
        refill_case.execute("C1", 10)


def test_refill_slot_invalid_quantity(vending_machine_with_no_money):
    refill_case = RefillSlotCase(vending_machine_with_no_money)
    with pytest.raises(ValueError, match="Quantity must be greater than 0"):
        refill_case.execute("A1", -5)
