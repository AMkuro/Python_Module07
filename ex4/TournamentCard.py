from typing import Any

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health)

        self._wins: int = 0
        self._losses: int = 0
        self._base_rating: int = 1200

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        base = super().play(game_state)
        return {
            **base,
            "effect": f"Tournament card {self._name} ready for battle",
        }

    def attack(self, target: Card) -> dict[str, Any]:
        target_name = (
            target._name if isinstance(target, Card) else str(target)
        )
        return {
            "attacker": self._name,
            "target": target_name,
            "damage": self._attack,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        damage_blocked = min(self._health // 2, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self._health = max(0, self._health - damage_taken)
        return {
            "defender": self._name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self._health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "name": self._name,
            "attack": self._attack,
            "health": self._health,
            "max_health": self._max_health,
        }

    def calculate_rating(self) -> int:
        win_bonus = self._wins * 16
        loss_penalty = self._losses * 16
        return self._base_rating + win_bonus - loss_penalty

    def update_wins(self, wins: int) -> None:
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "name": self._name,
            "wins": self._wins,
            "losses": self._losses,
            "rating": self.calculate_rating(),
            "record": f"{self._wins}-{self._losses}",
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        rank_info = self.get_rank_info()
        combat_stats = self.get_combat_stats()
        return {
            **rank_info,
            **combat_stats,
        }
