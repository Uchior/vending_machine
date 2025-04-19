import pytest
from vending_machine.domain.models.drink import Drink, Temperature
from vending_machine.domain.models.money import Money
from vending_machine.domain.models.slot import Slot
from vending_machine.domain.models.vending_machine import VendingMachine


@pytest.fixture(scope="function")
def fresh_slots():
    slots = {
        "A1": Slot(
            slot_number="A1",
            drink=Drink(name="Coke", price=120, temperature=Temperature.COLD),
            stock=5
        ),
        "B1": Slot(
            slot_number="B1",
            drink=Drink(name="Pepsi", price=130, temperature=Temperature.COLD),
            stock=0
        ),
    }
    return slots


@pytest.fixture(scope="function")
def vending_machine_with_no_money(fresh_slots):
    return VendingMachine(slots=fresh_slots, cash_reserve=Money(1000))


@pytest.fixture(scope="function")
def vending_machine_with_inserted_money(fresh_slots):
    vending_machine = VendingMachine(slots=fresh_slots, cash_reserve=Money(1000))
    vending_machine.insert_money(Money(200))
    return vending_machine
