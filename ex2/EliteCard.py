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
    _RANGED_ATTACK_THRESHOLD: int = 8
    _MAGIC_ATTACK_THRESHOLD: int = 6
    _SPELL_MANA_COST: int = 4
    _BLOCK_DIVISOR: int = 2

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
        if attack >= EliteCard._RANGED_ATTACK_THRESHOLD:
            return CombatType.RANGED
        elif attack >= EliteCard._MAGIC_ATTACK_THRESHOLD:
            return CombatType.MAGIC
        else:
            return CombatType.MELEE

    def attack(self, target: Card) -> dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target.name if isinstance(target, Card) else str(target),
            "damage": self.attack_power,
            "combat_type": self._combat_type.value,
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
            "combat_type": self._combat_type.value,
        }

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        base: dict[str, Any] = super().play(game_state)
        return {
            **base,
            "effect": f"Elite card {self.name} "
            f"({self._combat_type.value.capitalize()}) "
            f"ready for combat and magic",
        }

    def cast_spell(
        self, spell_name: str, targets: list[Card]
    ) -> dict[str, Any]:
        mana_cost = self._SPELL_MANA_COST
        if self.mana < mana_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "success": False,
                "error": "Insufficient mana",
            }
        self.mana -= mana_cost
        target_names = [
            t.name if isinstance(t, Card) else str(t) for t in targets
        ]
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": target_names,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self.mana = max(
            0,
            min(self.max_mana, self.mana + amount),
        )
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "mana": self.mana,
            "max_mana": self.max_mana,
        }
