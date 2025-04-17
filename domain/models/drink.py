from dataclasses import dataclass
from enum import Enum


class Temperature(Enum):
    HOT = "hot"
    COLD = "cold"


@dataclass(frozen=True)
class Drink:
    name: str
    temperature: Temperature
    price: int  # 日本円

    def __str__(self):
        return f"{self.name} ({self.temperature.value}) - ${self.price}"

    def __repr__(self):
        return f"Drink(name={self.name}, temperature={self.temperature}, price={self.price})"
