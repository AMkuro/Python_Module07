from abc import ABC
from typing import Any


class Card(ABC):
    class InstanceRule(Exception):
        pass

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__game_state = {}

    def play(self, game_state: dict) -> dict:
        mandatory_keys: dict[str, Any] = {
            "health": int,
            "battlefield": list[str],
            "mana_used": int,
        }
        for key, value in game_state.items():
            if key not in mandatory_keys:
                raise ValueError("There is unknown key")
            self.__game_state.update({key: value})

    def _ensure_validate(self) -> None:
        if not all(
            isinstance(value, str) for value in [self.__name, self.__rarity]
        ):
            raise ValueError(
                "name and rarity must be an str object, got {type("
            )
        if not isinstance(self.__cost, int):
            raise ValueError("cost have to be int")

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        if self.__cost <= available_mana:
            return True
        return False
