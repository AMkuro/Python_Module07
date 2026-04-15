import unittest

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from ex4.TournamentCard import TournamentCard


class CardPropertyTests(unittest.TestCase):
    def test_card_metadata_uses_mutable_public_attributes(self) -> None:
        card = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

        self.assertEqual(card.name, "Fire Dragon")
        self.assertEqual(card.cost, 5)
        self.assertEqual(card.rarity, Rarity.LEGENDARY)
        card.name = "Other Dragon"
        card.cost = 8
        self.assertEqual(card.get_card_info()["name"], "Other Dragon")
        self.assertEqual(card.get_card_info()["cost"], 8)


class CombatAndMagicPropertyTests(unittest.TestCase):
    def test_elite_card_exposes_mutable_public_combat_and_magic_attributes(
        self,
    ) -> None:
        card = EliteCard("Arcane Warrior", 5, Rarity.RARE, 6, 4, 8)

        self.assertEqual(card.attack_power, 6)
        self.assertEqual(card.health, 4)
        self.assertEqual(card.max_health, 4)
        self.assertEqual(card.mana, 8)
        self.assertEqual(card.max_mana, 8)
        card.attack_power = 9
        card.mana = 3
        self.assertEqual(card.get_combat_stats()["attack"], 9)
        self.assertEqual(card.get_magic_stats()["mana"], 3)


class TournamentPropertyTests(unittest.TestCase):
    def test_tournament_card_keeps_record_state_internal(
        self,
    ) -> None:
        card = TournamentCard("Arena Knight", 4, Rarity.RARE, 5, 5)

        card.update_wins(2)
        card.update_losses(1)

        self.assertFalse(hasattr(card, "wins"))
        self.assertFalse(hasattr(card, "losses"))
        rank_info = card.get_rank_info()
        self.assertEqual(rank_info["wins"], 2)
        self.assertEqual(rank_info["losses"], 1)


if __name__ == "__main__":
    unittest.main()
