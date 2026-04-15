from typing import Any

from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    _MANA_BUDGET: int = 5
    _HIGH_THREAT_THRESHOLD: int = 2
    _CREATURE_PRIORITY: int = 0
    _DAMAGE_SPELL_PRIORITY: int = 1
    _OTHER_PRIORITY: int = 2

    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        cards_played: list[str] = []
        played_cards: list[Card] = []
        mana_used: int = 0
        damage_dealt: int = 0
        remaining_mana: int = self._MANA_BUDGET

        cards_only = [c for c in hand if isinstance(c, Card)]
        sorted_hand = sorted(
            cards_only,
            key=lambda card: (self._get_play_priority(card), card.cost),
        )

        for card in sorted_hand:
            if card.cost > remaining_mana:
                continue
            cards_played.append(card.name)
            played_cards.append(card)
            mana_used += card.cost
            remaining_mana -= card.cost
            damage_dealt += self._estimate_damage(card)

        enemy_targets = [
            target.name
            for target in self.prioritize_targets(battlefield)
            if isinstance(target, Card)
        ]
        targets_attacked: list[str] = []
        if damage_dealt > 0:
            targets_attacked = enemy_targets or ["Enemy Player"]

        enemy_count = len(enemy_targets)
        priority_level = (
            "high" if enemy_count > self._HIGH_THREAT_THRESHOLD else "medium"
        )

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "played_cards": played_cards,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
            "battlefield_threats": enemy_count,
            "aggression_level": priority_level,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        combat_targets = [
            target
            for target in available_targets
            if isinstance(target, Card)
            and target.get_card_info().get("health") is not None
        ]
        if not combat_targets:
            return []
        return sorted(
            combat_targets,
            key=lambda target: target.health,
        )

    def _get_play_priority(self, card: Card) -> int:
        card_info = card.get_card_info()
        card_type = card_info.get("type")
        if card_type == "Creature":
            return self._CREATURE_PRIORITY
        if (
            card_type == "Spell"
            and card_info.get("effect_type") == "damage"
        ):
            return self._DAMAGE_SPELL_PRIORITY
        return self._OTHER_PRIORITY

    def _estimate_damage(self, card: Card) -> int:
        card_info = card.get_card_info()
        if card_info.get("type") == "Creature":
            return card_info.get("attack", 0)
        if (
            card_info.get("type") == "Spell"
            and card_info.get("effect_type") == "damage"
        ):
            return card.cost
        return 0
