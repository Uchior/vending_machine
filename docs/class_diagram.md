```mermaid
classDiagram
class VendingMachine {
- List~Slot~ slots
- CoinStorage coinStorage
- BillStorage billStorage
- CardPaymentOptions cardOptions
}

    class Slot {
        - String slotNumber
        - Drink drink
        - int stock
    }

    class Drink {
        - String name
        - int price
        - enum Temperature { HOT, COLD }
    }

    class CoinStorage {
        - Map~CoinType, int~ coins
    }

    class BillStorage {
        - Map~BillType, int~ bills
    }

    class CardPaymentOptions {
        - List~CardType~ acceptedCards
    }

    class RefillService
    class ReplaceDrinkService
    class UpdatePaymentOptionsService
    class CollectCashService

    VendingMachine --> Slot
    VendingMachine --> CoinStorage
    VendingMachine --> BillStorage
    VendingMachine --> CardPaymentOptions
```
