from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: Rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available_mana = game_state.get("mana", 0)
        if not self.is_playable(available_mana):
            raise ValueError(
                f"Not enough mana to play {self.name}"
                f" (cost: {self.cost}, available: {available_mana})"
            )
        self.result_dict: dict[str, Any] = {}
        result_dict: dict[str, Any] = {
            "card_played": self.name,
            "mana_used": self.cost,
        }
        return result_dict

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
        }

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana
