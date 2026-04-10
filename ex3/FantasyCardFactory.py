from typing import Any, Union

from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, EffectType
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creature_types: dict[str, tuple[int, int]] = {
            "dragon": (7, 5),
            "goblin": (2, 3),
        }
        self._spell_types: dict[str, EffectType] = {
            "fireball": EffectType.DAMAGE,
        }
        self._artifact_types: dict[str, int] = {
            "mana_ring": 5,
        }

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self._creature_types
        ):
            attack, health = self._creature_types[name_or_power]
            return CreatureCard(
                name=name_or_power.capitalize(),
                cost=attack + health - 1,
                rarity=Rarity.RARE,
                attack=attack,
                health=health,
            )
        return CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity=Rarity.RARE,
            attack=7,
            health=5,
        )

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self._spell_types
        ):
            effect_type = self._spell_types[name_or_power]
            return SpellCard(
                name=name_or_power.capitalize(),
                cost=3,
                rarity=Rarity.COMMON,
                effect_type=effect_type,
            )
        return SpellCard(
            name="Fireball",
            cost=3,
            rarity=Rarity.COMMON,
            effect_type=EffectType.DAMAGE,
        )

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if (
            isinstance(name_or_power, str)
            and name_or_power in self._artifact_types
        ):
            durability = self._artifact_types[name_or_power]
            return ArtifactCard(
                name=name_or_power.replace("_", " ").capitalize(),
                cost=2,
                rarity=Rarity.UNCOMMON,
                durability=durability,
                effect=f"+1 {name_or_power.split('_')[0]}",
            )
        return ArtifactCard(
            name="Mana Ring",
            cost=2,
            rarity=Rarity.UNCOMMON,
            durability=5,
            effect="+1 mana per turn",
        )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck_cards: list[Card] = []
        for i in range(size):
            if i % 3 == 0:
                deck_cards.append(self.create_creature())
            elif i % 3 == 1:
                deck_cards.append(self.create_spell())
            else:
                deck_cards.append(self.create_artifact())
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
