from typing import Any

from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: Rarity, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError(
                f"attack must be a positive integer, got {attack}"
            )
        if not isinstance(health, int) or health <= 0:
            raise ValueError(
                f"health must be a positive integer, got {health}"
            )
        self._attack: int = attack
        self._health: int = health

    def get_card_info(self) -> dict[str, Any]:
        base = super().get_card_info()
        return {
            **base,
            "type": "Creature",
            "attack": self._attack,
            "health": self._health,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        result = super().play(game_state)
        result["effect"] = "Creature summoned to battlefield"
        return result

    def attack_target(self, target: Card) -> dict[str, Any]:
        target_info = target.get_card_info()
        return {
            "attacker": self._name,
            "target": target_info["name"],
            "damage_dealt": self._attack,
            "combat_resolved": True,
        }
