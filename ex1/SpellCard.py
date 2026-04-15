from enum import Enum
from typing import Any

from ex0.Card import Card, Rarity


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: Rarity, effect_type: EffectType
    ) -> None:
        super().__init__(name, cost, rarity)
        self._effect_type: EffectType = effect_type

    def get_card_info(self) -> dict[str, Any]:
        base = super().get_card_info()
        return {
            **base,
            "type": "Spell",
            "effect_type": self._effect_type.value,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        result_dict: dict[str, Any] = super().play(game_state)
        effect_description = self._get_effect_description()
        result_dict["effect"] = effect_description
        return result_dict

    def _get_effect_description(self) -> str:
        effect_messages = {
            EffectType.DAMAGE: f"Deal {self.cost} damage to target",
            EffectType.HEAL: f"Heal {self.cost} health",
            EffectType.BUFF: f"Buff target by {self.cost}",
            EffectType.DEBUFF: f"Debuff target by {self.cost}",
        }
        return effect_messages.get(
            self._effect_type,
            f"Cast {self._effect_type.value} effect",
        )

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        return {
            "spell": self.name,
            "effect_type": self._effect_type.value,
            "targets": targets,
            "resolved": True,
        }
