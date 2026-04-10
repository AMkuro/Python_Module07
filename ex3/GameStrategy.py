from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        pass
