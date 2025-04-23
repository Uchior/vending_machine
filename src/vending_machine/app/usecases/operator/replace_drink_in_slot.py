from dataclasses import dataclass
from vending_machine.domain.models.vending_machine import VendingMachine
from vending_machine.domain.models.drink import Drink, Temperature
from vending_machine.domain.models.slot import Slot


@dataclass
class DrinkInputDTO:
    name: str
    price: int
    temperature: str


class ReplaceDrinkInSlotCase:
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine

    def execute(self, slot_number: str, new_drink_data: DrinkInputDTO, new_stock: int) -> str:
        if new_stock < 0:
            raise ValueError("New stock must be at least 0")
        if new_drink_data.price < 0:
            raise ValueError("New drink price must be at least 0")
        try:
            temp = Temperature(new_drink_data.temperature)
        except ValueError:
            raise ValueError("Temperature must be 'cold' or 'hot'")

        drink = Drink(name=new_drink_data.name, price=new_drink_data.price, temperature=temp)

        if slot_number in self.vending_machine.slots:
            slot = self.vending_machine.slots[slot_number]
            slot.replace_drink(drink, new_stock)
            action = "置き換えました"
        else:
            self.vending_machine.slots[slot_number] = Slot(slot_number=slot_number, drink=drink, stock=new_stock)
            action = "新しく追加しました"

        return f"{slot_number} に商品 '{drink.name}' ({drink.temperature.value}) を {new_stock} 本{action}。"
