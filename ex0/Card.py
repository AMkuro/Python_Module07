from abc import ABC
from typing import Any


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.__name: str = name
        self.__cost: int = cost
        self.__rarity: str = rarity
        self.__game_state: dict[str, Any] = {}

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
        return self.__game_state

    def _ensure_validate(self) -> None:
        self._ensure_numeric_validate(self.__cost)
        self._ensure_text_validate(self.__name, self.__rarity)

    def _ensure_text_validate(self, *test_strs: str) -> None:
        for value in test_strs:
            if not isinstance(value, str):
                raise ValueError(
                    f"{value=} must be an str object, got {type(value)}"
                )

    def _ensure_numeric_validate(self, *test_num: int | float) -> None:
        for value in test_num:
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"{value=} must be an int or"
                    f" float object, got {type(value)}"
                )

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        if self.__cost <= available_mana:
            return True
        return False
