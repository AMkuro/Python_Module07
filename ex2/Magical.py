from abc import ABC, abstractmethod
from typing import Any

from ex0.Card import Card


class Magical(ABC):
    def __init__(self, mana: int) -> None:
        self.mana: int = mana
        self.max_mana: int = mana

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: list[Card]
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        pass
