from typing import Any

from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self._effect_type: str = effect_type

    def get_card_info(self) -> dict[str, Any]:
        base = super().get_card_info()
        return {**base, "type": "Spell", "effect_type": self._effect_type}

    def play(self, game_state: dict) -> dict:
        result_dict = super().play(game_state)
        if self._effect_type == "damage":
            result_dict["effect"] = f"Deal {self._cost} damage to target"
        elif self._effect_type == "heal":
            result_dict["effect"] = f"Heal {self._cost} health"
        elif self._effect_type == "buff":
            result_dict["effect"] = f"Buff target by {self._cost}"
        elif self._effect_type == "debuff":
            result_dict["effect"] = f"Debuff target by {self._cost}"
        else:
            result_dict["effect"] = f"Cast {self._effect_type} effect"
        return result_dict

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self._name,
            "effect_type": self._effect_type,
            "targets": targets,
            "resolved": True,
        }
