from enum import Enum
from typing import Any

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"
    MAGIC = "magic"


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int,
        mana: int,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack, health)
        Magical.__init__(self, mana)
        self._combat_type: CombatType = (
            self._select_combat_type_by_attack(attack)
        )

    @staticmethod
    def _select_combat_type_by_attack(attack: int) -> CombatType:
        if attack >= 8:
            return CombatType.RANGED
        elif attack >= 6:
            return CombatType.MAGIC
        else:
            return CombatType.MELEE

    def attack(self, target: Card) -> dict[str, Any]:
        return {
            "attacker": self._name,
            "target": target._name
            if isinstance(target, Card)
            else str(target),
            "damage": self._attack,
            "combat_type": self._combat_type.value,
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
            "combat_type": self._combat_type.value,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        base: dict[str, Any] = super().play(game_state)
        return {
            **base,
            "effect": f"Elite card {self._name} "
            f"({self._combat_type.value.capitalize()}) "
            f"ready for combat and magic",
        }

    def cast_spell(
        self, spell_name: str, targets: list[Card]
    ) -> dict[str, Any]:
        mana_cost = 4
        if self._mana < mana_cost:
            return {
                "caster": self._name,
                "spell": spell_name,
                "success": False,
                "error": "Insufficient mana",
            }
        self._mana -= mana_cost
        target_names = [
            t._name if isinstance(t, Card) else str(t) for t in targets
        ]
        return {
            "caster": self._name,
            "spell": spell_name,
            "targets": target_names,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self._mana = min(self._max_mana, self._mana + amount)
        return {
            "channeled": amount,
            "total_mana": self._mana,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "name": self._name,
            "mana": self._mana,
            "max_mana": self._max_mana,
        }
