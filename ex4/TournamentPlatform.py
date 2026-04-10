from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = (
            card._name.lower().replace(" ", "_")
            + f"_{len(self._cards) + 1:03d}"
        )
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        if card1_id not in self._cards or card2_id not in self._cards:
            return {"error": "Invalid card IDs"}

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        card1_damage = getattr(card1, "_attack", 0)
        card2_damage = getattr(card2, "_attack", 0)

        if card1_damage > card2_damage:
            winner_id = card1_id
            loser_id = card2_id
            winner = card1
            loser = card2
        else:
            winner_id = card2_id
            loser_id = card1_id
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list[tuple[str, int, str]]:
        leaderboard: list[tuple[str, int, str]] = []
        for card_id, card in self._cards.items():
            rank_info = card.get_rank_info()
            rating = rank_info["rating"]
            record = rank_info["record"]
            leaderboard.append((card._name, rating, record))
        return sorted(leaderboard, key=lambda x: x[1], reverse=True)

    def generate_tournament_report(self) -> dict[str, Any]:
        if not self._cards:
            return {
                "total_cards": 0,
                "matches_played": 0,
                "avg_rating": 0,
                "platform_status": "empty",
            }

        ratings = [card.calculate_rating() for card in self._cards.values()]
        avg_rating = int(sum(ratings) / len(ratings))

        return {
            "total_cards": len(self._cards),
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
