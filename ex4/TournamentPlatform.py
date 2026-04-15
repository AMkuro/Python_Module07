from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0
        self._type_counters: dict[str, int] = {}

    def register_card(self, card: TournamentCard) -> str:
        last_word = card.name.split()[-1].lower()
        count = self._type_counters.get(last_word, 0) + 1
        self._type_counters[last_word] = count
        card_id = f"{last_word}_{count:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        if card1_id not in self._cards or card2_id not in self._cards:
            return {"error": "Invalid card IDs"}

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]
        comparison = card1.compare_to(card2)
        if comparison > 0:
            winner_id, winner, loser_id, loser = (
                card1_id,
                card1,
                card2_id,
                card2,
            )
        elif comparison < 0:
            winner_id, winner, loser_id, loser = (
                card2_id,
                card2,
                card1_id,
                card1,
            )
        elif card1_id <= card2_id:
            winner_id, winner, loser_id, loser = (
                card1_id,
                card1,
                card2_id,
                card2,
            )
        else:
            winner_id, winner, loser_id, loser = (
                card2_id,
                card2,
                card1_id,
                card1,
            )

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list[tuple[str, str, int, str]]:
        leaderboard: list[tuple[str, str, int, str]] = []
        for card_id, card in self._cards.items():
            rank_info = card.get_rank_info()
            rating = rank_info["rating"]
            record = rank_info["record"]
            leaderboard.append((card_id, rank_info["name"], rating, record))

        def sort_by_rating(
            entry: tuple[str, str, int, str]
        ) -> int:
            return entry[2]

        return sorted(leaderboard, key=sort_by_rating, reverse=True)

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
