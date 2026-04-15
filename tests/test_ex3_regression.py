import unittest

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import EffectType, SpellCard
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


class AggressiveStrategyTests(unittest.TestCase):
    def test_prefers_creatures_and_damage_spells_over_artifacts(self) -> None:
        strategy = AggressiveStrategy()
        hand = [
            CreatureCard("Fire Dragon", 5, Rarity.RARE, 7, 5),
            CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 2, 3),
            SpellCard(
                "Lightning Bolt",
                3,
                Rarity.COMMON,
                EffectType.DAMAGE,
            ),
            ArtifactCard("Mana Ring", 2, Rarity.UNCOMMON, 5, "+1 mana"),
        ]

        turn_result = strategy.execute_turn(hand, [])

        self.assertEqual(
            turn_result["cards_played"],
            ["Goblin Warrior", "Lightning Bolt"],
        )
        self.assertEqual(turn_result["mana_used"], 5)
        self.assertEqual(turn_result["damage_dealt"], 5)
        self.assertEqual(turn_result["targets_attacked"], ["Enemy Player"])


class FantasyCardFactoryTests(unittest.TestCase):
    def test_supports_runtime_registration_of_new_card_types(self) -> None:
        factory = FantasyCardFactory()

        factory.register_spell_type(
            "shadow_bolt",
            display_name="Shadow Bolt",
            effect_type=EffectType.DAMAGE,
            cost=4,
            rarity=Rarity.RARE,
        )

        spell = factory.create_spell("shadow_bolt")

        self.assertEqual(spell.get_card_info()["name"], "Shadow Bolt")
        self.assertEqual(spell.get_card_info()["cost"], 4)
        self.assertIn("shadow_bolt", factory.get_supported_types()["spells"])

    def test_create_themed_deck_builds_aggressive_opening_hand(self) -> None:
        factory = FantasyCardFactory()

        deck = factory.create_themed_deck(3)
        names = [card.get_card_info()["name"] for card in deck["cards"]]

        self.assertEqual(
            names,
            ["Fire Dragon", "Goblin Warrior", "Lightning Bolt"],
        )


class GameEngineTests(unittest.TestCase):
    def test_battlefield_only_tracks_persistent_played_cards(self) -> None:
        engine = GameEngine()
        engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())

        turn_result = engine.simulate_turn()

        self.assertEqual(
            turn_result["actions"]["cards_played"],
            ["Goblin Warrior", "Lightning Bolt"],
        )
        self.assertEqual(turn_result["battlefield_analysis"]["total_units"], 1)


if __name__ == "__main__":
    unittest.main()
