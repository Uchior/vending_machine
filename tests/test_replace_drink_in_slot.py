from vending_machine.app.usecases.operator.replace_drink_in_slot import ReplaceDrinkInSlotCase, DrinkInputDTO


def test_replace_drink_in_existing_slot(vending_machine_with_no_money):
    replace_case = ReplaceDrinkInSlotCase(vending_machine_with_no_money)
    drink_input = DrinkInputDTO("Milk Tea", 200, "cold")
    result = replace_case.execute("A1", drink_input, 5)
    assert result == "A1 に商品 'Milk Tea' (cold) を 5 本置き換えました。"
    assert vending_machine_with_no_money.slots["A1"].drink.name == "Milk Tea"


def test_replace_drink_in_new_slot(vending_machine_with_no_money):
    replace_case = ReplaceDrinkInSlotCase(vending_machine_with_no_money)
    drink_input = DrinkInputDTO("Milk Tea", 200, "cold")
    result = replace_case.execute("C3", drink_input, 8)
    assert result == "C3 に商品 'Milk Tea' (cold) を 8 本新しく追加しました。"
    assert vending_machine_with_no_money.slots["C3"].drink.name == "Milk Tea"
