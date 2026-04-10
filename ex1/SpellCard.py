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
        if self._effect_type == EffectType.DAMAGE:
            result_dict["effect"] = f"Deal {self._cost} damage to target"
        elif self._effect_type == EffectType.HEAL:
            result_dict["effect"] = f"Heal {self._cost} health"
        elif self._effect_type == EffectType.BUFF:
            result_dict["effect"] = f"Buff target by {self._cost}"
        elif self._effect_type == EffectType.DEBUFF:
            result_dict["effect"] = f"Debuff target by {self._cost}"
        else:
            result_dict["effect"] = f"Cast {self._effect_type.value} effect"
        return result_dict

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        return {
            "spell": self._name,
            "effect_type": self._effect_type.value,
            "targets": targets,
            "resolved": True,
        }
