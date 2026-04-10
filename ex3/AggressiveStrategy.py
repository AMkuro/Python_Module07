from typing import Any

from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        cards_played: list[str] = []
        mana_used: int = 0
        targets_attacked: list[str] = []
        damage_dealt: int = 0

        sorted_hand = sorted(
            hand,
            key=lambda c: (
                c._cost if isinstance(c, Card) else float("inf")
            ),
        )

        for card in sorted_hand:
            if isinstance(card, Card):
                cards_played.append(card._name)
                mana_used += card._cost
                if hasattr(card, "_attack"):
                    damage_dealt += card._attack
                    targets_attacked.append("Enemy Player")

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        if not available_targets:
            return []
        return sorted(
            available_targets,
            key=lambda t: getattr(t, "_health", 0),
        )
