from typing import Any

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self._durability: int = durability
        self._effect: str = effect

    def get_card_info(self) -> dict[str, Any]:
        base = super().get_card_info()
        return {
            **base,
            "type": "Artifact",
            "durability": self._durability,
            "effect": self._effect,
        }

    def play(self, game_state: dict) -> dict:
        result_dict = super().play(game_state)
        result_dict["effect"] = f"Permanent: {self._effect}"
        return result_dict

    def activate_ability(self) -> dict:
        if self._durability <= 0:
            return {"activated": False, "reason": "Artifact destroyed"}
        self._durability -= 1
        return {
            "artifact": self._name,
            "effect": self._effect,
            "durability_remaining": self._durability,
        }
