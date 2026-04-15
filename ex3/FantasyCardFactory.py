from typing import Any

from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, EffectType
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    _DEFAULT_POWER_LEVEL: int = 5
    _MAX_POWER_LEVEL: int = 10
    _MIN_POWER_LEVEL: int = 1
    _DEFAULT_CREATURE_COST: int = 5
    _DEFAULT_SPELL_COST: int = 3
    _DEFAULT_ARTIFACT_COST: int = 2
    _DEFAULT_ARTIFACT_DURABILITY: int = 5
    _DEFAULT_THEME_PATTERN: tuple[tuple[str, str], ...] = (
        ("creature", "dragon"),
        ("creature", "goblin"),
        ("spell", "lightning_bolt"),
        ("artifact", "mana_ring"),
        ("spell", "fireball"),
        ("artifact", "wizard_staff"),
    )

    def __init__(self) -> None:
        self._creature_types: dict[str, tuple[str, int, Rarity, int, int]] = {
            "dragon": ("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5),
            "goblin": ("Goblin Warrior", 2, Rarity.COMMON, 2, 3),
        }
        self._spell_types: dict[
            str, tuple[str, int, Rarity, EffectType]
        ] = {
            "fireball": ("Fireball", 3, Rarity.COMMON, EffectType.DAMAGE),
            "ice_blast": ("Ice Blast", 3, Rarity.UNCOMMON, EffectType.DEBUFF),
            "lightning_bolt": (
                "Lightning Bolt",
                3,
                Rarity.COMMON,
                EffectType.DAMAGE,
            ),
        }
        self._artifact_types: dict[
            str, tuple[str, int, Rarity, int, str]
        ] = {
            "mana_ring": (
                "Mana Ring",
                2,
                Rarity.UNCOMMON,
                5,
                "+1 mana per turn",
            ),
            "wizard_staff": (
                "Wizard Staff",
                3,
                Rarity.RARE,
                4,
                "+1 spell power",
            ),
            "healing_crystal": (
                "Healing Crystal",
                2,
                Rarity.UNCOMMON,
                4,
                "Restore 1 health per turn",
            ),
        }

    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self._creature_types
        ):
            name, cost, rarity, attack, health = self._creature_types[
                name_or_power
            ]
            return CreatureCard(
                name=name,
                cost=cost,
                rarity=rarity,
                attack=attack,
                health=health,
            )
        power_level = self._DEFAULT_POWER_LEVEL
        if isinstance(name_or_power, int):
            power_level = max(
                self._MIN_POWER_LEVEL,
                min(name_or_power, self._MAX_POWER_LEVEL),
            )
        return CreatureCard(
            name="Fire Dragon",
            cost=self._DEFAULT_CREATURE_COST,
            rarity=Rarity.RARE,
            attack=power_level,
            health=power_level,
        )

    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self._spell_types
        ):
            name, cost, rarity, effect_type = self._spell_types[
                name_or_power
            ]
            return SpellCard(
                name=name,
                cost=cost,
                rarity=rarity,
                effect_type=effect_type,
            )
        cost = self._DEFAULT_SPELL_COST
        if isinstance(name_or_power, int):
            cost = max(
                self._MIN_POWER_LEVEL,
                min(name_or_power, self._MAX_POWER_LEVEL),
            )
        return SpellCard(
            name="Fireball",
            cost=cost,
            rarity=Rarity.COMMON,
            effect_type=EffectType.DAMAGE,
        )

    def create_artifact(
        self, name_or_power: str | int | None = None
    ) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self._artifact_types
        ):
            name, cost, rarity, durability, effect = self._artifact_types[
                name_or_power
            ]
            return ArtifactCard(
                name=name,
                cost=cost,
                rarity=rarity,
                durability=durability,
                effect=effect,
            )
        durability = self._DEFAULT_ARTIFACT_DURABILITY
        if isinstance(name_or_power, int):
            durability = max(
                self._MIN_POWER_LEVEL,
                min(name_or_power, self._MAX_POWER_LEVEL),
            )
        return ArtifactCard(
            name="Mana Ring",
            cost=self._DEFAULT_ARTIFACT_COST,
            rarity=Rarity.UNCOMMON,
            durability=durability,
            effect="+1 mana per turn",
        )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck_cards: list[Card] = []
        for i in range(size):
            card_type, card_key = self._DEFAULT_THEME_PATTERN[
                i % len(self._DEFAULT_THEME_PATTERN)
            ]
            if card_type == "creature":
                deck_cards.append(self.create_creature(card_key))
            elif card_type == "spell":
                deck_cards.append(self.create_spell(card_key))
            else:
                deck_cards.append(self.create_artifact(card_key))
        return {
            "cards": deck_cards,
            "size": len(deck_cards),
            "theme": "Fantasy",
        }

    def get_supported_types(self) -> dict[str, Any]:
        return {
            "creatures": list(self._creature_types.keys()),
            "spells": list(self._spell_types.keys()),
            "artifacts": list(self._artifact_types.keys()),
        }

    def register_creature_type(
        self,
        key: str,
        display_name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int,
    ) -> None:
        self._creature_types[key] = (
            display_name,
            cost,
            rarity,
            attack,
            health,
        )

    def register_spell_type(
        self,
        key: str,
        display_name: str,
        effect_type: EffectType,
        cost: int = _DEFAULT_SPELL_COST,
        rarity: Rarity = Rarity.COMMON,
    ) -> None:
        self._spell_types[key] = (
            display_name,
            cost,
            rarity,
            effect_type,
        )

    def register_artifact_type(
        self,
        key: str,
        display_name: str,
        effect: str,
        durability: int = _DEFAULT_ARTIFACT_DURABILITY,
        cost: int = _DEFAULT_ARTIFACT_COST,
        rarity: Rarity = Rarity.UNCOMMON,
    ) -> None:
        self._artifact_types[key] = (
            display_name,
            cost,
            rarity,
            durability,
            effect,
        )
