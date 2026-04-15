from typing import Any

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    _DEFAULT_BASE_RATING: int = 1200
    _RATING_CHANGE_PER_MATCH: int = 16
    _HEALTH_BOOST_PER_WIN: int = 2
    _MAX_HEALTH_MULTIPLIER: int = 2
    _BLOCK_DIVISOR: int = 2

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int,
        base_rating: int = _DEFAULT_BASE_RATING,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health)

        self._wins: int = 0
        self._losses: int = 0
        self._base_rating: int = base_rating
        self._base_max_health: int = self.max_health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        base = super().play(game_state)
        return {
            **base,
            "effect": f"Tournament card {self.name} ready for battle",
        }

    def attack(self, target: Card) -> dict[str, Any]:
        target_name = target.name if isinstance(target, Card) else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        damage_blocked = min(
            self.health // self._BLOCK_DIVISOR, incoming_damage
        )
        damage_taken = incoming_damage - damage_blocked
        self.health = max(0, self.health - damage_taken)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "attack": self.attack_power,
            "health": self.health,
            "max_health": self.max_health,
        }

    def calculate_rating(self) -> int:
        win_bonus = self._wins * self._RATING_CHANGE_PER_MATCH
        loss_penalty = self._losses * self._RATING_CHANGE_PER_MATCH
        return self._base_rating + win_bonus - loss_penalty

    def update_wins(self, wins: int) -> None:
        if wins > 0:
            self._wins += wins
            health_boost = wins * self._HEALTH_BOOST_PER_WIN
            self.max_health = min(
                self.max_health + health_boost,
                self._base_max_health * self._MAX_HEALTH_MULTIPLIER,
            )

    def update_losses(self, losses: int) -> None:
        if losses > 0:
            self._losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "wins": self._wins,
            "losses": self._losses,
            "rating": self.calculate_rating(),
            "record": f"{self._wins}-{self._losses}",
        }

    def compare_to(self, other: "TournamentCard") -> int:
        self_score = (
            self.attack_power,
            self.calculate_rating(),
            self.health,
        )
        other_score = (
            other.attack_power,
            other.calculate_rating(),
            other.health,
        )
        if self_score > other_score:
            return 1
        if self_score < other_score:
            return -1
        return 0

    def get_tournament_stats(self) -> dict[str, Any]:
        rank_info = self.get_rank_info()
        combat_stats = self.get_combat_stats()
        return {
            **rank_info,
            **combat_stats,
        }
