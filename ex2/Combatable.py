from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    def __init__(self, attack: int, health: int) -> None:
        self._attack: int = attack
        self._health: int = health
        self._max_health: int = health

    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        pass
