import unittest

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex2.EliteCard import EliteCard
from ex3.AggressiveStrategy import AggressiveStrategy
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


class AggressiveStrategyReviewTests(unittest.TestCase):
    def test_execute_turn_ignores_non_combat_targets(self) -> None:
        strategy = AggressiveStrategy()
        hand = [CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 2, 3)]
        battlefield = [
            ArtifactCard("Mana Ring", 2, Rarity.UNCOMMON, 5, "+1 mana"),
            CreatureCard("Frontline Orc", 3, Rarity.COMMON, 4, 4),
            "spectator",
        ]

        turn_result = strategy.execute_turn(hand, battlefield)

        self.assertEqual(turn_result["targets_attacked"], ["Frontline Orc"])


class EliteCardReviewTests(unittest.TestCase):
    def test_channel_mana_does_not_drop_below_zero(self) -> None:
        elite_card = EliteCard(
            "Arcane Warrior",
            5,
            Rarity.RARE,
            5,
            4,
            3,
        )

        mana_result = elite_card.channel_mana(-10)

        self.assertEqual(mana_result["total_mana"], 0)


class TournamentReviewTests(unittest.TestCase):
    def test_compare_to_prefers_attack_then_rating_then_health(
        self,
    ) -> None:
        veteran = TournamentCard(
            "Veteran Knight",
            4,
            Rarity.RARE,
            5,
            5,
            base_rating=1300,
        )
        rookie = TournamentCard(
            "Rookie Knight",
            4,
            Rarity.COMMON,
            5,
            6,
            base_rating=1100,
        )

        self.assertGreater(veteran.compare_to(rookie), 0)
        self.assertLess(rookie.compare_to(veteran), 0)

    def test_update_wins_caps_max_health_at_double_original_value(
        self,
    ) -> None:
        card = TournamentCard(
            "Fire Dragon",
            5,
            Rarity.RARE,
            7,
            5,
        )

        card.update_wins(10)
        card.update_wins(10)

        self.assertEqual(card.get_combat_stats()["max_health"], 10)

    def test_create_match_breaks_attack_ties_by_rating(self) -> None:
        platform = TournamentPlatform()
        veteran = TournamentCard(
            "Veteran Knight",
            4,
            Rarity.RARE,
            5,
            5,
            base_rating=1300,
        )
        rookie = TournamentCard(
            "Rookie Knight",
            4,
            Rarity.COMMON,
            5,
            6,
            base_rating=1100,
        )

        veteran_id = platform.register_card(veteran)
        rookie_id = platform.register_card(rookie)

        match_result = platform.create_match(veteran_id, rookie_id)

        self.assertEqual(match_result["winner"], veteran_id)
        self.assertEqual(match_result["loser"], rookie_id)


if __name__ == "__main__":
    unittest.main()
