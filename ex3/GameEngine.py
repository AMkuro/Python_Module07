from typing import Any

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0
        self._battlefield: list[Any] = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        if self._factory is None or self._strategy is None:
            return {"error": "Engine not configured"}

        deck = self._factory.create_themed_deck(3)
        cards = deck.get("cards", [])

        turn_result = self._strategy.execute_turn(cards, self._battlefield)

        self._turns_simulated += 1
        self._cards_created += len(cards)
        damage = turn_result.get("damage_dealt", 0)
        self._total_damage += damage

        self._battlefield.extend(cards)

        threat_level = turn_result.get("battlefield_threats", 0)
        aggression = turn_result.get("aggression_level", "low")

        return {
            "strategy": self._strategy.get_strategy_name(),
            "actions": {
                "cards_played": turn_result.get("cards_played", []),
                "mana_used": turn_result.get("mana_used", 0),
                "targets_attacked": turn_result.get(
                    "targets_attacked", []
                ),
                "damage_dealt": damage,
            },
            "battlefield_analysis": {
                "threats_detected": threat_level,
                "aggression_level": aggression,
                "total_units": len(self._battlefield),
            },
        }

    def get_engine_status(self) -> dict[str, Any]:
        strategy_name = (
            self._strategy.get_strategy_name() if self._strategy else "None"
        )
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
            "battlefield_units": len(self._battlefield),
        }
