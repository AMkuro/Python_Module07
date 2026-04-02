from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name: str = name
        self._cost: int = cost
        self._rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self._name,
            "cost": self._cost,
            "rarity": self._rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return self._cost <= available_mana
