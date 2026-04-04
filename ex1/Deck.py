import random
from typing import Any

from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards = self._cards + [card]

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.get_card_info()["name"] == card_name:
                self._cards = self._cards[:i] + self._cards[i + 1:]
                return True
        return False

    def shuffle(self) -> None:
        cards = list(self._cards)
        random.shuffle(cards)
        self._cards = cards

    def draw_card(self) -> Card:
        if not self._cards:
            raise ValueError("Deck is empty")
        card = self._cards[0]
        self._cards = self._cards[1:]
        return card

    def get_deck_stats(self) -> dict[str, Any]:
        total = len(self._cards)
        if total == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0,
            }
        creatures = sum(
            1 for c in self._cards if c.get_card_info().get("type") == "Creature"
        )
        spells = sum(
            1 for c in self._cards if c.get_card_info().get("type") == "Spell"
        )
        artifacts = sum(
            1 for c in self._cards if c.get_card_info().get("type") == "Artifact"
        )
        avg_cost = sum(c.get_card_info()["cost"] for c in self._cards) / total
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1),
        }
