from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name: str = name
        self._cost: int = cost
        self._rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana", 0)
        if not self.is_playable(available_mana):
            raise ValueError(
                f"Not enough mana to play {self._name}"
                f" (cost: {self._cost}, available: {available_mana})"
            )
        self.result_dict: dict[str, Any] = {}
        result_dict = {
            "card_played": self._name,
            "mana_used": self._cost,
        }
        return result_dict

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self._name,
            "cost": self._cost,
            "rarity": self._rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return self._cost <= available_mana
