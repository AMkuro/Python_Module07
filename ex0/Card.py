from abc import ABC


class Card(ABC):
    class InstanceRule(Exception):
        pass

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity

    def play(self, game_state: dict) -> dict:
        pass

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
