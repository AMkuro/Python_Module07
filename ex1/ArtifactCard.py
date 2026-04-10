from typing import Any

from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        durability: int,
        effect: str,
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

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        result_dict: dict[str, Any] = super().play(game_state)
        ability_info = self.activate_ability()
        if ability_info["activated"]:
            result_dict["effect"] = ability_info["description"]
        return result_dict

    def activate_ability(self) -> dict[str, Any]:
        if self._durability <= 0:
            return {"activated": False, "reason": "Artifact destroyed"}
        self._durability -= 1
        return {
            "activated": True,
            "description": f"Permanent: {self._effect}",
            "durability_remaining": self._durability,
        }
