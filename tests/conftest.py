import pytest
from domain.models.drink import Drink, Temperature
from domain.models.money import Money
from domain.models.slot import Slot
from domain.models.vending_machine import VendingMachine

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


@pytest.fixture
def vending_machine_with_no_money():
    return VendingMachine(slots=slots, cash_reserve=Money(1000))


@pytest.fixture
def vending_machine_with_inserted_money():
    vending_machine = VendingMachine(slots=slots, cash_reserve=Money(1000))
    vending_machine.insert_money(Money(200))
    return vending_machine
